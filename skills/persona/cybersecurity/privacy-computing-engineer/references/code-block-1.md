# code Example

```
PRIVACY-PRESERVING COMPUTATION MENTAL MODEL
============================================

     DATA OWNER A        DATA OWNER B        DATA OWNER C
          |                   |                   |
          v                   v                   v
  [Local Compute]       [Local Compute]     [Local Compute]
   DP noise added        DP noise added      DP noise added
          |                   |                   |
          +--------+----------+---------+---------+
                   |                   |
           [SMPC Protocol]      [HE Ciphertext]
           GMW / SPDZ           SEAL
                   |                   |
                   +--------+----------+
                            |
                    [TEE Aggregator]
                    SGX
                    Remote Attestation
                            |
                            v
                  [Privacy-Preserving
                     Result
                  (No raw data exposed
                   at any protocol step)

ADVERSARIAL MODEL MUST BE EXPLICIT AT EVERY LAYER:
  Semi-honest? Malicious? Covert? Threshold (t-of-n)?
```
