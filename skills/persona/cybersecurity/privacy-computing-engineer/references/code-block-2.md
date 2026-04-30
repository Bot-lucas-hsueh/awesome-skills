# Privacy Computing Scenario Examples

## Scenario 1 — Federated Learning for Medical Data (Cross-Hospital) (§9)

```
[Hospital 1-12] (Each EU country)
     |
     v
[Local Training with DP-SGD]  <-- Opacus or TF Privacy
  - Clip gradients at C = 1.0
  - Add Gaussian noise sigma = 1.5
  - Renyi accountant tracks per-round epsilon
     |
     v  (Only noisy gradients transmitted -- no raw data leaves hospital)
[Flower Federated Server]  <-- Run in neutral jurisdiction or SGX enclave
  - FedAvg aggregation
  - Optional: secure aggregation (PySyft) to hide individual hospital updates
     |
     v
[Global Model]
  - Total epsilon budget: define epsilon_total = 8 (moderate) over full training
  - With sigma=1.5, C=1.0, q=0.01 (sampling rate), 500 rounds → epsilon ~6-8
```

## Scenario 2 — SMPC and HE for Financial Analytics (§9)

**Option A — SMPC (SPDZ, recommended for 2-party):**

```python
# PySyft two-party SMPC example
import syft as sy

# Each bank holds their transaction tensor locally
# Secret-shared with FSS (Function Secret Sharing) protocol
bank_a_data = sy.Tensor([...]).tag("transactions").encrypt(protocol="fss")
bank_b_data = sy.Tensor([...]).tag("transactions").encrypt(protocol="fss")

# Joint statistics computed without either party seeing the other's data
joint_fraud_rate = (bank_a_data + bank_b_data).mean().get()
# Neither bank's raw tensor is ever exposed; result is plaintext aggregate
```

**Option B — CKKS Homomorphic Encryption:**

```python
import seal
# Bank A encrypts its data under shared evaluation key
# Bank B performs homomorphic operations on encrypted data
# Result decrypted only with threshold decryption requiring both parties
params = seal.EncryptionParameters(seal.scheme_type.ckks)
params.set_poly_modulus_degree(8192)
params.set_coeff_modulus(seal.CoeffModulus.Create(8192, [60, 40, 40, 60]))
context = seal.SEALContext(params)
# Compute sum of encrypted vectors -- no decryption until final step
```

## Scenario 3 — Zero-Knowledge Proof for Compliance (§9)

```
Public inputs:  total portfolio value P, concentration limit 25%
Private inputs (witness): individual loan amounts L_1, L_2, ..., L_n
Statement: for all i: L_i / P <= 0.25

Circuit constraints:
  1. Range check: L_i in [0, 2^64] for each i
  2. Sum constraint: L_1 + L_2 + ... + L_n = P  (public)
  3. Ratio constraint: L_i * 4 <= P for each i  (equivalent to L_i/P <= 0.25)
```

## Anti-Pattern 1 — Centralized Aggregation Server (FINO) (§10)

```
BAD — Federated In Name Only (FINO):
  # Central server receives and stores all model updates individually
  updates = [receive_model(hospital) for hospital in hospitals]
  global_model = average(updates)
  # Server sees every individual update; gradient inversion is possible;
  # no legal basis for processing PHI expressed in gradients.

GOOD — Genuine federation with secure aggregation:
  from syft.frameworks.torch.fl import utils
  # Secure aggregation: server only sees the sum, not individual updates
  updates = [hospital.send_masked_update(mask_key) for hospital in hospitals]
  global_model = utils.federated_avg(updates)
  # Individual updates are never visible to the aggregation server.
  # Layer DP-SGD (Opacus) on top before transmission for formal guarantee.
```

## Anti-Pattern 2 — DP Epsilon Misreporting (§10)

```
BAD — Ignoring composition across training rounds:
  epsilon_per_round = 0.1  # "Privacy budget per round"
  rounds = 1000
  # Developer claims: "total epsilon is still 0.1 because we reset each round"
  # WRONG: epsilon composes. Sequential composition: epsilon_total = 100.
  # epsilon = 100 provides essentially zero privacy protection.

GOOD — Renyi DP accounting across all rounds:
  from opacus.accountants import RDPAccountant
  accountant = RDPAccountant()
  for round_num in range(rounds):
      accountant.step(noise_multiplier=1.5, sample_rate=0.01)
  epsilon, best_alpha = accountant.get_privacy_spent(delta=1e-5)
  assert epsilon <= 8.0, f"Privacy budget exceeded: epsilon={epsilon}"
  # Track cumulative epsilon throughout training; halt if budget exhausted.
```

## Anti-Pattern 3 — SGX Without Remote Attestation (§10)

```
BAD — Deploying SGX without attestation:
  # "The server is in an SGX enclave, so data is protected."
  # User sends sensitive data to endpoint with NO verification that:
  #   (a) Endpoint is actually running SGX code (not a plain server)
  #   (b) SGX code matches the expected enclave (MRENCLAVE hash)
  #   (c) SGX firmware is patched against Foreshadow
  client.send(sensitive_data, endpoint="https://our-sgx-server.com")
  # This is security theater: any server can impersonate the enclave.

GOOD — Full remote attestation before data transmission:
  from gramine_ratls import verify_attestation
  quote, mrenclave = client.request_attestation(endpoint)
  verify_attestation(
      quote=quote,
      expected_mrenclave=TRUSTED_MRENCLAVE_HASH,
      min_svn=CURRENT_SECURITY_VERSION,
      ias_root_cert=INTEL_ROOT_CERT
  )
  # Only AFTER successful attestation:
  session_key = derive_session_key(quote)
  client.send(sensitive_data.encrypt(session_key))
```

## Anti-Pattern 4 — SMPC with Malicious Majority (§10)

```
BAD — Using semi-honest SMPC protocol with malicious parties:
  # GMW protocol is proven secure under SEMI-HONEST assumption only.
  # Team deploys GMW for 5-party computation; 3 parties are adversarial.
  # Malicious majority can extract inputs and produce wrong outputs undetected.
  result = gmw_protocol.compute(parties=5, my_input=secret_data)
  # "We use SMPC so it's secure" is incorrect when adversary controls 3/5.

GOOD — Select protocol matching actual adversarial assumption:
  # If malicious majority is possible, require honest majority (t < n/2)
  # OR use authenticated secret sharing (SPDZ) for malicious minority.
  from pysyft.frameworks.mpc import SPDZ
  result = SPDZ.compute(
      parties=parties,
      my_input=secret_data,
      security="malicious"  # Authenticated shares; abort-secure
  )
  # Document explicitly: "Security holds if < n/2 parties are malicious."
```

## Anti-Pattern 5 — HE Without Noise Budget Management (§10)

```
BAD — Exceeding HE noise budget silently:
  from seal import Evaluator
  ct = encryptor.encrypt(plaintext)
  for i in range(100):  # Deep circuit, no budget tracking
      ct = evaluator.multiply(ct, ct)  # Each multiply consumes budget
  result = decryptor.decrypt(ct)  # May return GARBAGE with no error thrown.
  # Silent correctness failure: result is meaningless noise.

GOOD — Track noise budget and plan circuit depth explicitly:
  ct = encryptor.encrypt(plaintext)
  print(f"Initial noise budget: {decryptor.invariant_noise_budget(ct)} bits")
  for op in circuit_ops:
      budget = decryptor.invariant_noise_budget(ct)
      if budget < MINIMUM_SAFE_BUDGET:
          # Refresh via relinearization + rescaling (CKKS) or bootstrapping
          ct = evaluator.relinearize(ct, relin_keys)
          ct = evaluator.rescale_to_next(ct)
      ct = evaluator.multiply(ct, op)
  # Use bootstrapping (OpenFHE) when budget approaches minimum threshold.
```
