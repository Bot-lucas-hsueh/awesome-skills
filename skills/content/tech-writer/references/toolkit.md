## § 7 · Professional Toolkit

The following tools are used in documentation production, review, and maintenance workflows:

| Tool | Purpose | When Used |
|---|---|---|
| **MkDocs Material** | Static site generator optimized for technical docs. Supports search, versioning, admonitions, and Mermaid diagrams natively. | Primary docs site for developer portals and SDK documentation. |
| **Docusaurus** | React-based static site generator maintained by Meta. Excellent for open-source projects needing versioned docs and i18n. | Open-source project documentation, API portals with versioning requirements. |
| **Sphinx** | Python documentation generator with autodoc support. Produces HTML and PDF from reStructuredText or Markdown. | Python libraries, projects requiring PDF output, academic/enterprise documentation. |
| **Vale** | Command-line prose linter that enforces style guide rules (Google, Microsoft, custom). Integrates with CI/CD and editors. | Every documentation PR. Catches style violations before human review. |
| **OpenAPI/Swagger UI** | Renders OpenAPI 3.x specs as interactive API explorers with try-it-now functionality. | API reference portals. Paired with Redoc for clean print-ready output. |
| **Postman** | API testing platform that exports collections as interactive documentation. Supports environment variables and code generation. | REST API documentation, developer onboarding, API testing workflows. |
| **Mermaid** | Markdown-native diagram syntax for flowcharts, sequence diagrams, ER diagrams, and architecture maps. | Architecture diagrams, API flow documentation, data model visualization — anything that would otherwise be a screenshot. |
| **Grammarly** | AI-powered grammar and clarity checker. Business plan enables style and tone consistency checks across a team. | Final review pass before publishing. Not a substitute for Vale or human review. |
| **Hemingway Editor** | Readability analyzer that highlights complex sentences, passive voice, and adverb overuse. Targets Grade 8-10 reading level. | Readability audit of existing docs. Onboarding new technical writers to the house style. |
| **Figma** | Design tool used to produce annotated screenshots, UI callout diagrams, and branded documentation illustrations. | UI-heavy documentation (user guides, admin guides). Screenshots are annotated in Figma, not raw captures. |
| **Loom** | Async video tool for recording short walkthroughs that supplement written documentation. | Complex multi-step setup procedures where video reduces ambiguity. Linked from docs, not embedded (avoids maintenance burden). |
| **Redoc** | OpenAPI reference documentation renderer with three-panel layout. | Clean, printable API documentation, particularly for external APIs. |

---
