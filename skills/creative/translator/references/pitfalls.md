## § 10 — Common Pitfalls

### Anti-Pattern 1: Literal Translation of Idioms

❌ **BAD:** Translating "it's raining cats and dogs" into French as "il pleut des chats et des chiens"
- Result: Meaningless, confusing, sounds absurd to native French speakers

✅ **GOOD:** Translating as "il pleut des cordes" (it's raining ropes — the French equivalent idiom)
- **Why it matters:** Idioms carry cultural-specific mental images; literal translation transfers the words but destroys the meaning. The goal is to transfer the reader's experience, not the dictionary words.

---

### Anti-Pattern 2: Ignoring Register Shifts

❌ **BAD:** Translating a formal legal contract into casual conversational language, or a casual app UI into stiff formal prose
- Example: Rendering a terms-of-service clause ("The User shall indemnify...") as "You'll cover us if..."
- Result: Wrong tone for context; undermines legal enforceability or brand voice

✅ **GOOD:** Matching the register of the source in the target — formal for formal, casual for casual
- **Why it matters:** Register carries social meaning. A contract in casual language may be unenforceable; an app in stiff legal prose will confuse users and harm conversion rates.

---

### Anti-Pattern 3: Translating Without a Glossary

❌ **BAD:** Translating "valve" as "válvula" in chapter 1, "valva" in chapter 3, and "compuerta" in chapter 7 of the same technical manual
- Result: Reader confusion; quality failure; possible safety risk if operators cannot match written terms to physical components

✅ **GOOD:** Building a 30-term glossary before starting; enforcing it throughout with TM
- **Why it matters:** Terminology consistency is not optional in technical and regulated content — it is a contractual quality requirement under ISO 17100 and a safety prerequisite in regulated industries.

---

### Anti-Pattern 4: Accepting MT Output Without Assessment

❌ **BAD:** Taking DeepL output and applying light post-editing to every segment regardless of MT quality assessment
- Example: A medical MT segment reads fluently but has silently flipped a negation ("do not exceed" → "exceed" due to syntax complexity)
- Result: Dangerous medical error that passed undetected because the output looked fluent

✅ **GOOD:** Assess MT quality before committing to PE scope; apply full PE (accuracy + fluency) for safety-critical content; never use light PE for medical, legal, or safety material
- **Why it matters:** MT generates plausible-sounding errors. Fluency is not accuracy. High-stakes content requires accuracy-first review regardless of MT quality.

---

### Anti-Pattern 5: Silent Adaptation Without Notes

❌ **BAD:** Transcreating a marketing tagline with completely different words and delivering it with no explanation to the client
- Result: Client rejects the "translation" because it "doesn't say what we wrote"; relationship damaged; rework required

✅ **GOOD:** Delivering transcreation with a clear explanation: "This is a transcreation. The source tagline relies on the English idiom X, which has no direct equivalent in Japanese. The proposed target text preserves your message of Y using culturally resonant imagery Z. Alternative: [option 2]."
- **Why it matters:** Transcreation decisions need client buy-in. Unexplained adaptations look like errors. Documented rationale transforms a potential rejection into a collaborative creative decision.

---

### Anti-Pattern 6: Ignoring Locale-Specific Formatting

❌ **BAD:** Leaving "January 15, 2026" in a German document, or "10,000.50" (US format) in a French document
- Result: European readers read the comma as a decimal separator — "10" becomes "10,000.50" → confusion

✅ **GOOD:** Applying locale-specific conventions: 15. Januar 2026 (German), 15 janvier 2026 (French); 10.000,50 (German), 10 000,50 (French)
- **Why it matters:** Locale formatting errors signal unprofessional work and can cause financial or scheduling errors for the reader.

---

### Anti-Pattern 7: Skipping Back-Translation on High-Stakes Content

❌ **BAD:** Delivering a medical patient information leaflet (PIL) without back-translation verification
- Result: A subtle meaning shift in dosage instructions goes undetected; patient safety risk

✅ **GOOD:** Back-translate 10% sample of high-stakes documents; review for meaning preservation vs. source
- **Why it matters:** Back-translation is the most reliable method for detecting meaning drift that looks fine in the target language. It is standard practice for clinical trial documentation and regulatory submissions.

---

