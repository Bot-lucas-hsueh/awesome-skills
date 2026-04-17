## § 7 · Standards & Reference

→ Full reference documentation: `references/07-standards.md`

**Permission Templates:**

| Template | Use Case | Description |
|----------|----------|-------------|
| `standard` | Open source projects | Public read, restricted submit |
| `restricted` | Internal projects | Registered users only, tight controls |
| `protected-branches` | Production branches | Multiple reviewer requirements |
| `multi-team` | Large organizations | Team-specific branches with cross-team read |
| `git-flow` | Git Flow workflows | Branch-role matrix for CD pipelines |

**Git Flow Permission Matrix:**

| Role | master | develop | feature/* | release/* | hotfix/* |
|------|--------|---------|-----------|-----------|----------|
| **Project Owners** | Submit, Push | Submit, Push | All | All | All |
| **Release Managers** | Submit (2+ reviews) | Submit | - | Submit, Create | Submit, Create |
| **Team Leads** | - | Submit (1+ review) | Submit, Create, Push | - | Create |
| **Developers** | - | Push | Create, Push | - | - |
| **CI Bot** | Verify | Verify | Verify | Verify | Verify |

---

## Phase 1: Discovery & Assessment

| Step | Action | Success Criteria |
|------|--------|------------------|
| 1.1 | Identify target repositories | [✓] Repository list compiled with owners |
| 1.2 | Map existing group structure | [✓] Group hierarchy documented |
| 1.3 | Analyze current permissions | [✓] Permission matrix exported |
| 1.4 | Classify repositories by sensitivity | [✓] Classification labels assigned |

**[✗] FAIL:** Cannot proceed without repository inventory and classification

### Phase 2: Design & Template Selection

| Step | Action | Success Criteria |
|------|--------|------------------|
| 2.1 | Select appropriate template per classification | [✓] Template-to-repo mapping complete |
| 2.2 | Customize branch protection rules | [✓] Branch patterns defined |
| 2.3 | Define group-to-permission mappings | [✓] Group permissions matrix created |
| 2.4 | Review design with stakeholders | [✓] Sign-off obtained |

**[✗] FAIL:** Do not proceed without stakeholder approval

### Phase 3: Validation & Testing

| Step | Action | Success Criteria |
|------|--------|------------------|
| 3.1 | Create test environment replica | [✓] Non-prod environment ready |
| 3.2 | Apply templates to test repos | [✓] Templates applied without errors |
| 3.3 | Execute permission test matrix | [✓] All test cases pass |
| 3.4 | Verify audit compliance | [✓] Security score ≥ 90% |

**[✗] FAIL:** Address all test failures before production deployment

### Phase 4: Production Deployment

| Step | Action | Success Criteria |
|------|--------|------------------|
| 4.1 | Backup current permissions | [✓] Export saved to version control |
| 4.2 | Deploy during maintenance window | [✓] Changes applied |
| 4.3 | Validate production functionality | [✓] Critical workflows verified |
| 4.4 | Run post-deployment audit | [✓] No drift detected |

**[✗] FAIL:** Rollback immediately if critical workflows fail

### Phase 5: Monitoring & Maintenance

| Step | Action | Success Criteria |
|------|--------|------------------|
| 5.1 | Enable drift detection | [✓] Baseline established |
| 5.2 | Schedule regular audits | [✓] Audit cadence defined |
| 5.3 | Document exceptions | [✓] Exception log maintained |
| 5.4 | Review and update templates | [✓] Quarterly review scheduled |

---

