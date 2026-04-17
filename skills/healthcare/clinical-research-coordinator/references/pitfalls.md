## 10. Common Pitfalls & Anti-Patterns

### 🔴 High Severity

**Anti-Pattern 1: Retroactive ICF Documentation

```markdown
❌ BAD: Subject enrolled on March 1; ICF signed on March 3 because "the printer was broken"
→ Invalid consent; all data from March 1-3 is unusable; FDA 483 observation

✅ GOOD: Delay enrollment until ICF is properly executed; document printer issue 
separately with IT ticket number; never backdate consent documents
```

**Anti-Pattern 2: Incomplete SAE Documentation

```markdown
❌ BAD: "Subject hospitalized for pneumonia. Treated with antibiotics. Now resolved."
→ Missing: onset date/time, severity criteria, causality assessment, action taken 
with study drug, outcome details

✅ GOOD: Use sponsor's standardized SAE form; complete all required fields; attach 
source documents; PI signature required within 48 hours
```

### 🟡 Medium Severity

**Anti-Pattern 3: Informal Protocol Waivers

```markdown
❌ BAD: PI says "just enroll this patient, we'll sort out the paperwork later"
→ Unapproved deviation; sponsor contract violation; potential data integrity issues

✅ GOOD: Require written protocol waiver from sponsor before any deviation; 
document in writing with justification; update consent if eligibility changes
```

**Anti-Pattern 4: Source Data Verification Skipped

```markdown
❌ BAD: CRF data entered from memory without source document verification
→ Data integrity concerns; FDA inspection finding; query rates increase

✅ GOOD: 100% SDV for critical data points (primary endpoints, safety); 10-20% 
SDV for other data per monitoring plan
```

