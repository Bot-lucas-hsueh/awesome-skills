## 7. Standards & Reference

**Diátaxis Framework — Four Documentation Quadrants:**

| Quadrant | Orientation | Answers | Format |
|---|---|---|---|
| **Tutorial** | Learning | "Can I learn this?" | Narrative, step-by-step, single outcome |
| **How-To Guide** | Task completion | "How do I achieve X?" | Numbered procedure, assumes competence |
| **Explanation** | Understanding | "Why does it work this way?" | Discursive prose, context, trade-offs |
| **Reference** | Information lookup | "What is the exact syntax for X?" | Tables, consistent structure, exhaustive |

**Google Developer Documentation Style Guide — Key Rules:**

- Use second person ("you") and active voice throughout.
- Introduce acronyms on first use: "Application Programming Interface (API)".
- Use "select" for UI options, "click" for buttons, "enter" for typed input, "run" for commands.
- Avoid: "simply", "just", "easy", "straightforward", "obvious", "trivial".
- Code formatting: all code, commands, file paths, parameter names, and variable names in code font.
- Heading capitalization: sentence case for all headings ("Configure the authentication" not "Configure The Authentication").

**Readability Metrics and Target Ranges:**

| Metric | Target | Measurement Tool |
|---|---|---|
| Flesch-Kincaid Grade Level | < 10 (general developer audience) | Hemingway Editor, Vale plugin |
| Average sentence length | < 20 words | Hemingway Editor |
| Passive voice percentage | < 5% of sentences | Hemingway Editor, Grammarly |
| Paragraph length | Maximum 3 sentences | Manual review, Vale custom rule |

**Documentation Coverage Metrics:**

| Metric | Target | Notes |
|---|---|---|
| Time-to-first-API-call | < 10 minutes | Measured from landing page to first successful 200 response |
| API method documentation coverage | 100% of public endpoints | Tracked via OpenAPI spec completeness check in CI |
| Search success rate | > 80% | % of searches resulting in session > 30 seconds on result page |
| User satisfaction (feedback widget) | > 4.0 / 5.0 | Embedded thumbs up/down with optional comment |
| Pages per visit | > 3.0 | Indicates documentation depth is being explored, not abandoned |
| Support ticket deflection rate | Tracked quarterly | Compare support volume before/after documentation updates |
