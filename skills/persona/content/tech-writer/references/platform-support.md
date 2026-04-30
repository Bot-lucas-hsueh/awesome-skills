## § 6 · Platform Support

| Platform | Session Install | Persistent Config |
|----------|-----------------|-------------------|
| **OpenCode** | `/skill install tech-writer` | Auto-saved to `~/.opencode/skills/` |
| **OpenClaw** | `Read [URL] and install as skill` | Auto-saved to `~/.openclaw/workspace/skills/` |
| **Claude Code** | `Read [URL] and install as skill` | Append to `~/.claude/CLAUDE.md` (global) |
| **Cursor** | Paste §1 into `.cursorrules` | Save to `~/.cursor/rules/tech-writer.mdc` (global) |
| **OpenAI Codex** | Paste §1 into system prompt | `~/.codex/config.yaml` → `system_prompt:` |
| **Cline** | Paste §1 into Custom Instructions | Append §1 to `.clinerules` (project) |
| **Kimi Code** | `Read [URL] and install as skill` | Append to `.kimi-rules` |

**[URL]:** `https://awesome-skills.dev/skills/content/tech-writer.md`

Before producing any documentation, consult these authoritative sources:

1. **Diátaxis Framework** — https://diataxis.fr/
   - The definitive source for documentation structure theory
   - Use to determine which quadrant your content belongs in

2. **Google Developer Documentation Style Guide** — https://developers.google.com/style
   - Word list (words to use and avoid)
   - Voice and tone guidelines
   - Formatting conventions

3. **Microsoft Writing Style Guide** — https://learn.microsoft.com/en-us/style-guide/
   - Standard for enterprise technical writing
   - Accessibility guidelines

4. **OpenAPI Specification** — https://spec.openapis.org/
   - For API reference documentation
   - Understanding OpenAPI 3.0/3.1 features

5. **MkDocs Material Documentation** — https://squidfunk.github.io/mkdocs-material/
   - For implementing docs-as-code sites
   - Admonitions, diagrams, and extensions

6. **Vale Documentation** — https://vale.sh/
   - For configuring prose linting
   - Custom style rule creation

**Workflow Integration:**
1. Before starting any document, identify which Diátaxis quadrant it serves
2. Check the appropriate style guide for formatting conventions
3. For API docs, validate against OpenAPI spec before publishing
4. Run Vale linting on all prose before finalizing

---
