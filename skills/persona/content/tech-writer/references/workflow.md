## 8. Standard Workflow

### Phase 1: API Documentation Sprint

**Input:** OpenAPI spec file, Postman collection, or engineer interview notes.

**Step 1 — Inventory [✓ Done: spec parsed; endpoint list complete]**
Parse the OpenAPI spec or Postman collection. Produce an endpoint inventory: method, path, authentication requirement, and a one-sentence description. Flag any endpoints missing descriptions, response schemas, or error codes.
[✗ FAIL: spec has no descriptions on > 20% of endpoints — return to engineer for annotation before proceeding]

**Step 2 — Authentication Documentation [✓ Done: auth flow documented with working code example]**
Document the authentication mechanism first. This is always the developer's first failure point. Include: credential acquisition, token format, header/parameter placement, token refresh flow, and a complete working cURL example with a real-format (not placeholder) response.
[✗ FAIL: code example uses placeholder credentials without a "how to get real credentials" link]

**Step 3 — Endpoint Reference [✓ Done: all endpoints documented; error codes resolved]**
For each endpoint, document: description (one sentence, starts with a verb), required and optional parameters (table format with type, constraints, description), request body schema (all fields, not "see model"), response schema (all fields, status codes including 4xx and 5xx), and code examples in at minimum cURL and one SDK language.
[✗ FAIL: any 5xx error code has "Contact support" as its only documentation]

**Step 4 — Review and Vale Linting [✓ Done: Vale passes with 0 errors; code examples tested]**
Run Vale against all new documentation. Fix all errors and warnings. Test every code example in a clean environment (fresh virtual environment, no pre-installed dependencies). Confirm every example returns the documented response.
[✗ FAIL: Vale reports errors; any code example fails to execute]

---

### Phase 2: Tutorial Creation with Diátaxis

**Input:** Feature specification, target audience definition, learning outcome statement.

**Step 1 — Define the Outcome [✓ Done: single measurable learning outcome written]**
Write one sentence: "By the end of this tutorial, the reader will have [specific, visible outcome]." If you cannot write this sentence, the tutorial scope is undefined. Narrow it until you can.
[✗ FAIL: outcome is "understand how X works" — that is Explanation, not Tutorial]

**Step 2 — Prerequisites List [✓ Done: prerequisites verified on clean environment]**
List every tool, account, permission, and configuration the reader needs before step 1. For each prerequisite, include the install command or signup link and the verification command ("Run `python --version`. You should see `3.11.x` or later.").
[✗ FAIL: any prerequisite lacks a verification step]

**Step 3 — Write the Steps [✓ Done: each step produces visible output; narrative is continuous]**
Write each step so it produces visible output the reader can verify. Steps are numbered. Each step has: what you're doing (one sentence), the command or action, and the expected output in a code block. The tutorial should feel like pair programming with an expert guide.
[✗ FAIL: two consecutive steps produce no visible output; reader cannot confirm they are on track]

**Step 4 — Completion Validation [✓ Done: "you've built X" statement; next steps linked]**
End with a clear statement of what was accomplished and three next steps the reader can take independently. Link to the relevant How-To Guides and Reference documentation.
[✗ FAIL: tutorial ends abruptly with no completion statement or next steps]
