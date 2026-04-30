## § 2 · What This Skill Does

This skill transforms raw technical inputs (code, specs, changelogs, design docs, interviews with engineers) into production-grade developer documentation. Specific capabilities include:

1. **API Reference Documentation** — Takes an OpenAPI/Swagger spec, Postman collection, or raw endpoint list and produces a complete, accurate, and scannable API reference. Includes authentication flows, request/response schemas with field-level descriptions, error codes with remediation steps, rate limiting documentation, and code samples in Python, JavaScript, cURL, and Go. Each endpoint is documented to the standard: what it does, what it needs, what it returns, what can go wrong.

2. **Tutorial Design (Diátaxis-Compliant)** — Designs and writes tutorials that teach by doing. Tutorials have a clear narrative arc: safe starting state → guided steps → working outcome. Each step produces visible output so the learner knows they are on track. Tutorials never explain why (that belongs in Explanation docs) — they guide through a curated path to success.

3. **How-To Guide Development** — Creates task-oriented guides that help developers accomplish specific goals. Unlike tutorials, how-to guides assume the reader has baseline knowledge and jumps straight to the procedure. Multiple paths to the same outcome are documented when applicable.

4. **Explanation Documents** — Writes conceptual documentation that helps readers understand why a system works the way it does. Explains architecture decisions, design patterns, and underlying principles. Uses analogies and diagrams to make abstract concepts concrete.

5. **Reference Documentation** — Produces comprehensive reference material: API docs, CLI manuals, configuration guides, error code catalogs. Optimized for scanning and lookup, not linear reading. Uses tables, schemas, and structured data.

6. **Docs-as-Code Implementation** — Configures and documents documentation pipelines using MkDocs Material, Docusaurus, or Sphinx. Sets up Vale for prose linting against Google or Microsoft style guides, integrates OpenAPI spec rendering, configures CI/CD gates that fail the build when documentation coverage drops below threshold, and writes the contributing guide so engineers can maintain docs alongside code.

7. **Documentation Quality Measurement** — Defines and tracks documentation health metrics: time-to-first-API-call (target: < 10 minutes from landing page to working request), documentation coverage (% of public API methods with complete reference entries), Flesch-Kincaid readability (target: Grade Level < 10 for general developer audience), search success rate (% of in-docs searches that result in a page visit > 30 seconds), and user satisfaction via embedded feedback widgets.

8. **Documentation Audit** — Reviews existing documentation for completeness, accuracy, accessibility, and freshness. Identifies gaps, outdated content, missing examples, and structural issues. Provides prioritized recommendations with effort estimates.

---
