## 10. Common Pitfalls & Anti-Patterns

### 🔴 High Severity

**Anti-Pattern 1: Headline Repetition Without Analysis

```markdown
❌ BAD:
"The Federal Reserve held rates steady at 5.25–5.50% today."
[No context, no implication, no recommendation — zero analyst value added]

✅ GOOD:
"VERDICT: Fed hold was expected, but the statement's labor market language shift
('somewhat elevated' → 'moderately elevated') is a dovish micro-signal markets
have not fully priced — watch the June dot plot for confirmation.
Evidence: Fed funds futures moved from 42% to 51% probability of June cut
within 2h of the statement release."
```

**Anti-Pattern 2: Unverified Breaking News Presented as Fact

```markdown
❌ BAD:
"Reports suggest China is preparing to ban Nvidia GPU exports to third countries.
This will significantly impact AI infrastructure globally."
[Single-source, unverified, high-confidence framing for a speculative claim]

✅ GOOD:
"🔮 SPECULATIVE: A single Taiwanese trade publication reports Chinese regulators
are studying GPU re-export controls. Zero corroboration from Reuters/AP/SCMP.
If confirmed, downstream impact is material (Nvidia Asia revenue ~28% of total)
— monitoring closely. Do not act on this until corroborated."
```

### 🟡 Medium Severity

**Anti-Pattern 3: GitHub Stars = Quality

```markdown
❌ BAD:
"awesome-chatgpt-prompts gained 8,000 stars today — this is a must-watch repository
for AI practitioners."
[Star velocity is driven by social virality, not engineering value]

✅ GOOD:
Apply Hype Calibration Matrix:
- Stars velocity: 8,000/day → High hype signal
- Contributor profile: 1 maintainer, last commit 3 months ago → Low quality signal
- Production evidence: no deployments, no enterprise case studies → Low
- Verdict: Viral content collection, not engineering infrastructure. Low priority.
```

**Anti-Pattern 4: Siloed Domain Analysis

```markdown
❌ BAD:
[Four separate sections with no connections between them — geopolitics, finance,
AI, and GitHub analyzed as if they exist in separate universes]

✅ GOOD:
Cross-Domain Synthesis section explicitly maps:
"EU AI Act enforcement pressure (§1) + DeepSeek open-source momentum (§4) =
European enterprises face a new sourcing decision tree. Map the implication chain."
```

