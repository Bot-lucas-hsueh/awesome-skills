## § 9 — Scenario Examples

### Scenario A: Technical Manual — English → German

**User:** "Translate this safety instruction from our robot arm manual: 'Torque the mounting bolt to 45 Nm ± 5 Nm. Do not exceed maximum rated torque. Overtightening will cause permanent damage to the joint assembly.'"

**Translator Analysis:**
- Domain: Industrial mechanical — safety-critical instruction
- Register: Technical-formal, imperative voice
- Cultural delta: None for Germany (Nm is international SI unit; no conversion needed)
- German technical manuals use infinitive imperatives ("anziehen") not Sie-form imperatives
- Key terms: "torque" (verb) = "anziehen mit"; "torque" (noun) = "Anzugsmoment" (fastener context, not "Drehmoment" which is physics); "joint assembly" = "Gelenkbaugruppe"; "mounting bolt" = "Befestigungsschraube"
- Stakes: High — safety instruction; recommend review by German-market technical writer

**Translation:**
"Befestigungsschraube mit 45 Nm ± 5 Nm anziehen. Das maximale Nennanzugsmoment nicht überschreiten. Übermäßiges Anziehen führt zu dauerhaften Schäden an der Gelenkbaugruppe."

**Translator's Notes:**
1. "Anzugsmoment" selected over "Drehmoment" — "Anzugsmoment" is the established term for fastener torque in German mechanical engineering; "Drehmoment" is the general physics term
2. "dauerhaften Schäden" (permanent damage) — "dauerhaft" preferred over "bleibend" for technical register
3. German compounds "Gelenkbaugruppe" — natural German technical formation, no space

---

### Scenario B: Marketing Transcreation — English → Chinese (Simplified)

**User:** "Transcreate this tagline for the Chinese market: 'Break the mold. Be bold. Be you.'"

**Translator Analysis:**
- Domain: Marketing — tagline
- Register: Creative, informal, aspirational
- Cultural delta: HIGH — "break the mold" is a culture-specific idiom with no natural Chinese equivalent; literal 打破模具 (break the mold/tool) is meaningless in this context
- Target audience: Chinese consumers, likely 18–35, aspirational lifestyle brand
- Transcreation required: preserve spirit of nonconformity and self-expression, adapt form completely
- Rhythm consideration: Chinese taglines work best in 4/4 or 3/3 character groupings for memorability

**Transcreation options:**

Option 1 (Recommended): **"突破常规，活出自我"**
- Literal back-translation: "Break conventions, live as yourself"
- Rhythm: 4+4 characters — aesthetically natural in Chinese
- Tone: Bold, empowering, aspirational — matches source intent
- Cultural fit: High — "活出自我" is a well-established aspirational phrase in contemporary Chinese

Option 2 (Alternative): **"与众不同，做真实的你"**
- Literal back-translation: "Be different from the crowd, be your authentic self"
- Slightly softer; "与众不同" well-established; longer (8 characters) less punchy

**Recommendation:** Option 1 — tighter, more memorable, better rhythm, captures brand boldness.

**Note:** This is transcreation — the words are completely different from the English source. Client approval required as the meaning is preserved but form is transformed.

---

### Scenario C: Legal Clause — English → French (Belgium)

**User:** "I need to translate this force majeure clause for a Belgian contract: 'Neither party shall be liable for any failure or delay in performance if such failure or delay is caused by circumstances beyond that party's reasonable control, including but not limited to acts of God, war, government regulations, or natural disasters.'"

**Translator Analysis:**
- Domain: Legal — contract clause, civil law jurisdiction
- Register: Formal-legal — precise, unambiguous
- Target jurisdiction: Belgium — civil law system (unlike UK/US common law)
- Critical legal delta: French law has its own "force majeure" doctrine under Article 1218 of the French Civil Code (applicable in Belgium via Belgian Civil Code alignment), which has specific requirements: the event must be (1) unforeseeable, (2) irresistible, and (3) external. The English common-law formulation is broader.
- "Shall" (mandatory obligation) must render as "sera" or "ne sera pas" — preserving obligatory sense
- "Reasonable control" has no exact Belgian civil law equivalent — "contrôle raisonnable" is used but interpreted under civil law doctrine
- "Acts of God" has no civil law concept — typically rendered as "cas fortuits ou de force majeure" in French legal tradition

**Translation:**
"Aucune des parties ne sera responsable de tout manquement ou retard dans l'exécution de ses obligations si ce manquement ou retard résulte de circonstances indépendantes de la volonté raisonnable de cette partie, y compris, sans s'y limiter, les cas de force majeure, les actes de guerre, les réglementations gouvernementales ou les catastrophes naturelles."

**Translator's Notes:**
1. "Acts of God" → "cas de force majeure" — no direct civil law equivalent for the common-law concept; "cas de force majeure" is the established Belgian/French legal term covering extraordinary external events
2. "Shall be liable" → "sera responsable" — "sera" preserves mandatory/obligatory sense in French
3. IMPORTANT: The scope of "force majeure" under Belgian law (Article 1218 Belgian Civil Code) is narrower than this common-law clause implies. A Belgian-qualified attorney should review whether the clause as translated creates the intended contractual protection under Belgian civil law.

---

### Scenario D: MTPE Assessment — Software UI (EN → ES)

**User:** "DeepL translated our app's settings screen. Here are 3 segments — assess MT quality and post-edit."

**Source | MT Output | Assessment:**

1. "Notification preferences" | "Preferencias de notificación" | ✓ Accept as-is — standard term, accurate
2. "Allow app to send you personalized recommendations based on your usage" | "Permitir que la aplicación le envíe recomendaciones personalizadas según su uso" | ⚠ Light edit — "le envíe" (usted-form) inconsistent with app's tuteo (tú-form) throughout; change to "te envíe"
3. "Tap to toggle sound on/off" | "Toca para activar/desactivar el sonido" | ⚠ Light edit — "activar/desactivar" correct; however "Toca" (tú imperative) — verify tú/usted consistency; if tú, correct

**Post-edited output:**
1. "Preferencias de notificación" (unchanged)
2. "Permitir que la aplicación **te** envíe recomendaciones personalizadas según tu uso"
3. "Toca para activar/desactivar el sonido" (if tú confirmed) or "Toque para activar/desactivar el sonido" (if usted)

**MTPE Note:** MT quality is Good for this content type — estimated light PE effort (1 hour per 1000 words). Consistency issue (tú/usted) is common in MT output; requires full document pronoun consistency pass before delivery.

---

