# Gerrit Permission Templates

Predefined permission configurations for common scenarios.

## Standard Template

For typical open source projects with balanced access control.

```json
{
  "description": "Standard open source project permissions",
  "refs/heads/main": {
    "read": ["Anonymous Users"],
    "submit": ["Project Owners", "Maintainers"],
    "label-Code-Review": {
      "-2..+2": ["Maintainers", "Project Owners"],
      "-1..+1": ["Registered Users"]
    },
    "label-Verified": {
      "-1..+1": ["CI Bot", "Maintainers"]
    }
  },
  "refs/heads/develop": {
    "read": ["Anonymous Users"],
    "submit": ["Developers", "Maintainers"],
    "label-Code-Review": {
      "-1..+1": ["Registered Users"]
    }
  },
  "refs/tags/*": {
    "pushTag": ["Maintainers"],
    "pushSignedTag": ["Project Owners"]
  }
}
```

## Restricted Template

High-security projects with limited access.

```json
{
  "description": "Restricted access permissions",
  "refs/heads/main": {
    "read": ["Registered Users"],
    "submit": ["Project Owners"],
    "label-Code-Review": {
      "-2..+2": ["Project Owners"],
      "-1..+1": ["Maintainers"]
    },
    "label-Verified": {
      "-1..+1": ["CI Bot", "Project Owners"]
    }
  },
  "refs/heads/*": {
    "read": ["Registered Users"],
    "create": ["Maintainers"],
    "push": ["Maintainers"]
  },
  "refs/tags/*": {
    "pushTag": ["Project Owners"],
    "pushSignedTag": ["Project Owners"]
  }
}
```

## Protected Branches Template

Strict main branch protection with mandatory reviews.

```json
{
  "description": "Protected branches with mandatory reviews",
  "refs/heads/main": {
    "read": ["Anonymous Users"],
    "submit": ["Project Owners"],
    "label-Code-Review": {
      "-2..+2": ["Project Owners", "Senior Maintainers"],
      "-1..+1": ["Registered Users"]
    },
    "require-minimum-code-review-score": 2,
    "require-approval-count": 2
  },
  "refs/heads/release/*": {
    "read": ["Anonymous Users"],
    "submit": ["Release Managers", "Project Owners"],
    "label-Code-Review": {
      "-2..+2": ["Release Managers"]
    }
  },
  "refs/heads/feature/*": {
    "read": ["Registered Users"],
    "create": ["Registered Users"],
    "push": ["Registered Users"],
    "submit": ["Maintainers"]
  }
}
```

## Multi-Team Template

Multiple teams with different access levels.

```json
{
  "description": "Multi-team access configuration",
  "teams": {
    "backend-team": ["Backend Developers"],
    "frontend-team": ["Frontend Developers"],
    "devops-team": ["DevOps Engineers"],
    "qa-team": ["QA Engineers"]
  },
  "refs/heads/main": {
    "read": ["All Teams"],
    "submit": ["Tech Leads", "Project Owners"],
    "label-Code-Review": {
      "-2..+2": ["Tech Leads"],
      "-1..+1": ["All Teams"]
    }
  },
  "refs/heads/backend/*": {
    "read": ["backend-team", "devops-team"],
    "submit": ["backend-team-leads"],
    "push": ["backend-team"]
  },
  "refs/heads/frontend/*": {
    "read": ["frontend-team", "devops-team"],
    "submit": ["frontend-team-leads"],
    "push": ["frontend-team"]
  },
  "refs/heads/infrastructure/*": {
    "read": ["devops-team"],
    "submit": ["devops-team-leads"],
    "push": ["devops-team"]
  }
}
```

## CI/CD Integration Template

Permissions optimized for automated CI/CD workflows.

```json
{
  "description": "CI/CD optimized permissions",
  "service-accounts": {
    "ci-bot": "jenkins@example.com",
    "release-bot": "release@example.com"
  },
  "refs/heads/main": {
    "read": ["Anonymous Users"],
    "submit": ["Project Owners", "CI Bot Account"],
    "label-Code-Review": {
      "-2..+2": ["Maintainers"],
      "-1..+1": ["Registered Users"]
    },
    "label-Verified": {
      "-1..+1": ["CI Bot Account"]
    }
  },
  "refs/for/refs/heads/main": {
    "push": ["Registered Users"],
    "label-Code-Review": {
      "-1..+1": ["Registered Users"]
    }
  },
  "refs/tags/*": {
    "pushTag": ["Release Bot Account"],
    "pushSignedTag": ["Project Owners"]
  }
}
```

## Git Flow Template

Complete Git Flow workflow implementation with branch-based permissions. See [git-flow.md](git-flow.md) for detailed documentation.

```json
{
  "description": "Git Flow workflow permissions",
  "branches": {
    "master": {
      "permissions": {
        "read": ["Anonymous Users"],
        "submit": ["Project Owners", "Release Managers"],
        "label-Code-Review": {
          "-2..+2": ["Project Owners", "Release Managers"],
          "-1..+1": ["Registered Users"]
        }
      },
      "requirements": {
        "minCodeReviewScore": 2,
        "requiredReviewers": 2,
        "blockDirectPush": true
      }
    },
    "develop": {
      "permissions": {
        "read": ["Registered Users"],
        "submit": ["Project Owners", "Release Managers", "Team Leads"],
        "label-Code-Review": {
          "-2..+2": ["Team Leads", "Release Managers"],
          "-1..+1": ["Developers"]
        }
      },
      "requirements": {
        "minCodeReviewScore": 1,
        "requiredReviewers": 1
      }
    },
    "feature/*": {
      "permissions": {
        "read": ["Registered Users"],
        "create": ["Developers", "Team Leads"],
        "push": ["Developers", "Team Leads"],
        "submit": ["Team Leads", "Release Managers"],
        "delete": ["Developers", "Team Leads"]
      }
    },
    "release/*": {
      "permissions": {
        "read": ["Registered Users"],
        "create": ["Release Managers", "Project Owners"],
        "push": ["Release Managers", "Project Owners"],
        "submit": ["Release Managers", "Project Owners"],
        "label-Code-Review": {
          "-2..+2": ["Release Managers"]
        }
      },
      "requirements": {
        "minCodeReviewScore": 2,
        "requiredReviewers": 2
      }
    },
    "hotfix/*": {
      "permissions": {
        "read": ["Registered Users"],
        "create": ["Release Managers", "Project Owners", "Team Leads"],
        "push": ["Release Managers", "Project Owners"],
        "submit": ["Release Managers", "Project Owners"],
        "label-Code-Review": {
          "-2..+2": ["Release Managers", "Project Owners"]
        }
      },
      "requirements": {
        "minCodeReviewScore": 1,
        "requiredReviewers": 1
      }
    }
  },
  "groups": {
    "Project Owners": { "permissions": ["all"] },
    "Release Managers": { "permissions": ["submit_master", "submit_release", "submit_hotfix"] },
    "Team Leads": { "permissions": ["submit_develop", "submit_feature"] },
    "Developers": { "permissions": ["create_feature", "push_feature"] },
    "CI Bot": { "permissions": ["label-Verified"] }
  }
}
```

### Git Flow Role Permissions

| Role | master | develop | feature/* | release/* | hotfix/* |
|------|--------|---------|-----------|-----------|----------|
| **Project Owners** | Submit, Push | Submit, Push | All | All | All |
| **Release Managers** | Submit (2+ reviews) | Submit | - | Submit, Create | Submit, Create |
| **Team Leads** | - | Submit (1+ review) | Submit, Create, Push | - | Create |
| **Developers** | - | Push | Create, Push | - | - |
| **CI Bot** | Verify | Verify | Verify | Verify | Verify |

### Using Git Flow Template

```bash
# Apply to single repository
./scripts/apply-permissions.sh --repo myproject --template git-flow

# Apply to all repos in manifest
./scripts/bulk-update.sh --manifest default.xml --template git-flow
```

## Template Usage

Apply a template using the apply-permissions script:

```bash
./scripts/apply-permissions.sh --repo myproject --template standard
./scripts/apply-permissions.sh --repo myproject --template restricted
./scripts/apply-permissions.sh --repo myproject --template protected-branches
./scripts/apply-permissions.sh --repo myproject --template multi-team
./scripts/apply-permissions.sh --repo myproject --template ci-cd
./scripts/apply-permissions.sh --repo myproject --template git-flow
```

## Custom Template

Create custom templates by extending existing ones:

```bash
# Copy existing template
cp references/templates/standard.json references/templates/custom.json

# Edit and customize
# Then apply
./scripts/apply-permissions.sh --repo myproject --template custom
```
