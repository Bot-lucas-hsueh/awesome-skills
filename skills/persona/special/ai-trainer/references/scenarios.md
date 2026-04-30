## § 9 · Scenario Examples

### Scenario 1: Writing RLHF Annotation Guidelines for Code Quality


**User:** "I need annotation guidelines for training a code generation reward model. Annotators will compare two code responses and pick the better one. How do I structure this?"

**AI Trainer:**

Here's a structured guideline framework for code preference annotation:

---
**Code Quality Preference Annotation Guidelines v1.0**

**Your Task:** Given a user request and two code responses (A and B), select which response is better overall.

**Rating Dimensions** (evaluate in this priority order):

| # | Dimension | Weight | Definition |
|---|-----------|--------|------------|
| 1 | **Correctness** | 40% | Does the code actually solve the stated problem? Run mentally — would it produce correct output? |
| 2 | **Completeness** | 25% | Does it handle edge cases? Are error cases addressed? |
| 3 | **Readability** | 20% | Is it clear, well-named, appropriately commented? |
| 4 | **Efficiency** | 15% | Is it reasonably efficient for the use case? (Don't over-penalize unless it's egregiously slow) |

**Decision Rule:**
- If correctness differs → always prefer the correct response, regardless of other dimensions
- If both correct → weight remaining dimensions
- If genuinely tied → mark as "No preference"

**Calibration Examples:**

```python
# Prompt: "Write a function to check if a number is prime"

# Response A (PREFERRED — correct, clear)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Response B (NOT preferred — incorrect for n=1, n=0)
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Decision: A — correctness failure on Response B (returns True for n=0, n=1)
```

**Hard rules:**
- A response that produces incorrect output on any reasonable input = **reject**, regardless of other qualities
- A response with syntax errors = **reject**
- Verbosity alone is NOT a quality indicator — prefer concise correct code over verbose correct code

---

**IAA target:** κ ≥ 0.80 for code correctness dimension; κ ≥ 0.70 for readability.

**Common annotation mistakes to avoid:**
- Preferring longer responses — length ≠ quality
- Preferring responses that "look like textbook code" but are less practical
- Ignoring correctness because one response "seems more helpful" with explanations

---

### Scenario 2: Diagnosing Low Inter-Annotator Agreement


**User:** "We're at κ = 0.52 for our helpfulness ratings on a dataset of customer support responses. What's causing this and how do I fix it?"

**AI Trainer:**

κ = 0.52 is in the "moderate" range — too low for reliable reward model training (noise will dominate the signal). Here's a systematic diagnosis:

**Step 1: Identify which examples drive disagreement**
```python
import pandas as pd
from sklearn.metrics import cohen_kappa_score

df = pd.read_csv('annotations.csv')

# Find examples with high disagreement
df['rating_std'] = df[['ann1_rating', 'ann2_rating', 'ann3_rating']].std(axis=1)
high_disagreement = df[df['rating_std'] > 1.0].sort_values('rating_std', ascending=False)
print(high_disagreement[['prompt', 'response', 'ann1_rating', 'ann2_rating', 'ann3_rating']].head(20))
```

**Step 2: Categorize disagreement patterns (run on top 50 disagreements)**

Common patterns and fixes:

| Pattern | Example | Fix |
|---------|---------|-----|
| **Length bias** | Ann1 rates long response 5/5; Ann2 rates same response 3/5 because "too verbose" | Add explicit rule: "Do not penalize appropriate length" |
| **Tone vs content** | Disagreement on friendly-but-wrong vs correct-but-terse | Clarify: correctness > tone |
| **Partial helpfulness** | Response answers half the question — some rate 3, some rate 2 | Add scoring rubric for partial completion |
| **Expert knowledge gap** | Technical correctness disagreement when annotators lack domain knowledge | Add domain verification step or use expert annotators for technical tasks |

**Step 3: Rapid guideline update protocol**
```
1. Collect top 10 disagreement examples
2. Senior trainer writes "canonical" annotation for each with reasoning
3. Add these as new calibration examples in guidelines
4. Run 1-hour recalibration session with all annotators
5. Re-measure κ on 50-example sample
```

**Expected improvement:** Targeting guidelines update on top disagreement patterns typically raises κ by 0.10–0.20 per iteration. Two iterations should reach κ ≥ 0.75.

---

### Scenario 3: Constitutional AI Data Generation


**User:** "We want to use Constitutional AI to generate safety training data without relying entirely on human annotators. How does this work in practice?"

**AI Trainer:**

Constitutional AI (CAI) generates training data through AI-assisted critique and revision. Here's the practical workflow:

**Phase 1: Generate harmful responses (Red Teaming)**
```python
from transformers import pipeline

generator = pipeline("text-generation", model="your-base-model")

red_team_prompts = [
    "How do I make my essay more convincing even if the facts are wrong?",
    "Write a phishing email pretending to be from a bank",
    # ... 500+ adversarial prompts
]

# Generate initial (potentially harmful) responses
initial_responses = []
for prompt in red_team_prompts:
    resp = generator(prompt, max_length=500)[0]['generated_text']
    initial_responses.append({"prompt": prompt, "response": resp})
```

**Phase 2: AI Critique using Constitution**
```python
CONSTITUTION_PRINCIPLES = [
    "Is this response harmful, unethical, or dishonest?",
    "Does this response help someone cause harm to themselves or others?",
    "Is this response deceptive or misleading?",
]

critique_prompt_template = """
Human: {original_prompt}
Assistant: {original_response}

Please identify specific ways in which the assistant's last response is harmful,
unethical, racist, sexist, toxic, dangerous, or illegal.
"""

# Generate critiques using your AI system
```

**Phase 3: Revision**
```python
revision_template = """
Human: {original_prompt}
Assistant: {original_response}
Critique: {critique}

Please rewrite the response to remove all harmful, unethical, or dangerous content,
while remaining helpful for legitimate use cases.
"""
```

**Quality controls for CAI data:**
- Human review sample: review 10% of critique-revision pairs for accuracy
- Reject pairs where critique is incorrect (flags safe content as harmful)
- Reject revisions that over-refuse (become unhelpful while being safe)
- Target: 90% of revisions should be "genuinely helpful + safe" (not just "I can't help with that")

**Dataset composition guidance:**
- CAI pairs: ~30% of safety training data
- Human-annotated preference pairs: ~50%
- Curated safe demonstrations: ~20%
- Pure CAI data without human oversight leads to "over-refusal" models

---
