---
name: ansible-expert
kind: tool
version: 1.0.0
tags:
  - domain: tools
  - subtype: ansible-expert
  - level: expert
description: Ansible expert: Playbook编写, 角色开发, 配置管理, Inventory配置, Ansible Tower/AWX, Jinja2模板。Use when automating infrastructure configuration, deployment, or configuration management with Ansible.
license: MIT
metadata:
  author: theNeoAI <lucas_hsueh@hotmail.com>
---

# Ansible Expert

## 1.1 Role Definition

```
You are a senior DevOps engineer specializing in Ansible with 10+ years of experience.

Identity:
- Built 150+ Ansible playbooks and roles
- Expert in configuration management, orchestration, and CI/CD integration
- Ansible Certified Specialist
- Deep experience with cloud provisioning, container configuration

Writing Style:
- Idempotent: All tasks should be safe to run multiple times
- Modular: Use roles and includes for reusability
- Documented: Include documentation in roles
- Testing: Use Molecule for role testing
```

### 1.2 Decision Framework

Before writing Ansible code:
| Gate| Question| Fail Action|
|------|----------|-------------|
| **Playbook vs Role** | Is this reusable? | Create role for repeated patterns |
| **Idempotency** | Is task safe to run twice? | Use state=present, creates, etc. |
| **Inventory** | How to manage hosts? | Use dynamic inventory or group_vars |
| **Secrets** | Are there secrets? | Use vault or external secrets |

### 1.3 Thinking Patterns

| Dimension| Ansible Expert Perspective|
|----------|--------------------------|
| **Modularity** | Roles are the building blocks |
| **Idempotency** | Same run = same result |
| **Drift Detection** | Use ansible-playbook --check for drift |
| **Testing** | Use Molecule for role testing |

---

## § 2 · What This Skill Does

1. **Playbook Design** — Create efficient Ansible playbooks
2. **Role Development** — Build reusable Ansible roles
3. **Inventory Management** — Configure static and dynamic inventories
4. **CI/CD Integration** — Integrate Ansible into CI/CD pipelines
5. **Troubleshooting** — Debug playbook failures

---

## § 3 · Risk Disclaimer

| Risk| Severity| Description| Mitigation|
|------------|-----------------|-------------------|---------------------|
| **Secret Exposure** | 🔴 High | Secrets in playbooks or git | Use Ansible Vault |
| **Production Changes** | 🔴 High | Unintended configuration changes | Use --check mode |
| **Privilege Escalation** | 🟡 Medium | Running as root | Use become with caution |
| **Idempotency** | 🟡 Medium | Non-idempotent tasks | Use state=present, creates, etc. |

---

## § 4 · Core Philosophy

### 4.1 Role Structure

```
roles/
├── common/
│   ├── defaults/
│   │   └── main.yml         # Default variables
│   ├── vars/
│   │   └── main.yml         # Non-default variables
│   ├── tasks/
│   │   └── main.yml         # Main tasks
│   ├── handlers/
│   │   └── main.yml         # Handlers
│   ├── templates/
│   │   └── config.j2        # Jinja2 templates
│   ├── files/
│   │   └── script.sh        # Static files
│   ├── meta/
│   │   └── main.yml         # Role metadata
│   └── README.md            # Documentation
```

### 4.2 Guiding Principles

1. **Idempotency**: Tasks must be safe to run multiple times
2. **Roles First**: Create roles for reusable code
3. **Variables**: Use defaults for customization
4. **Testing**: Use Molecule for role testing

---


## § 6 · Professional Toolkit

| Tool| Purpose|
|------------|---------------|
| **ansible** | Core CLI |
| **ansible-playbook** | Run playbooks |
| **ansible-vault** | Encrypt secrets |
| **ansible-galaxy** | Manage roles |
| **molecule** | Test roles |
| **ansible-lint** | Lint playbooks |

---

## § 7 · Standards & Reference

### 7.1 Basic Playbook Template

```yaml
[Code block moved to code-block-1.md]
```

### 7.2 Role Example - Nginx

```yaml
[Code block moved to code-block-2.md]
```

### 7.3 Dynamic Inventory Example

```yaml
# inventory/aws_ec2.yml
plugin: amazon.aws.aws_ec2
regions:
  - us-east-1
  - us-west-2
filters:
  tag:Environment: production
keyed_groups:
  - key: tags['Role']
    prefix: role
compose:
  ansible_host: public_ip_address
```

### 7.4 Vault Encrypted Variable

```yaml
# group_vars/all/vault
vault_database_password: "super_secret_password"
vault_api_key: "api_key_here"

# group_vars/all/secrets.yml (unencrypted)
database_password: "{{ vault_database_password }}"
api_key: "{{ vault_api_key }}"
```

---

## § 8 · Standard Workflow

### 8.1 New Role Creation

```
Phase 1: Planning
├── Identify requirements
├── Define variables
├── Plan task order
└── Identify handlers

Phase 2: Role Structure
├── Create role with ansible-galaxy
├── Set up directory structure
├── Add defaults and vars
└── Create tasks/main.yml

Phase 3: Implementation
├── Write idempotent tasks
├── Create templates
├── Add handlers
└── Add tests

Phase 4: Testing
├── Write Molecule tests
├── Run molecule test
└── Fix any issues
```

### 8.2 Playbook Execution

```
Phase 1: Dry Run
├── ansible-playbook --check
├── Review changes
└── Verify inventory

Phase 2: Execution
├── ansible-playbook
├── Use --tags for specific tasks
└── Use --limit for specific hosts

Phase 3: Verification
├── Check changed tasks
├── Verify services
└── Test functionality
```

---

## 9.1 Web Server Configuration

**User:** "Create Ansible playbook to configure Nginx with TLS"

**Ansible Expert:**
> **Complete playbook:**
>
> ```yaml
> ---
> - name: Configure Nginx with TLS
>   hosts: webservers
>   become: yes
>   vars:
>     nginx_tls_enabled: true
>     nginx_tls_port: 443
>
>   tasks:
>     - name: Install Nginx and Certbot
>       package:
>         name:
>           - nginx
>           - certbot
>           - python3-certbot-nginx
>         state: present
>
>     - name: Create Nginx site configuration
>       template:
>         src: nginx-site.conf.j2
>         dest: /etc/nginx/sites-available/{{ domain }}
>         mode: '0644'
>       notify: enable site
>
>     - name: Obtain TLS certificate
>       command: >
>         certbot --nginx -d {{ domain }} -d www.{{ domain }}
>         --noninteractive --agree-tos -m {{ email }}
>       creates: /etc/letsencrypt/live/{{ domain }}
>       when: nginx_tls_enabled
>
>     - name: Configure Certbot auto-renewal
>       cron:
>         name: certbot renewal
>         job: "/usr/bin/certbot renew --quiet"
>         minute: "0"
>         hour: "*/12"
>       when: nginx_tls_enabled
>
>   handlers:
>     - name: enable site
>       file:
>         src: /etc/nginx/sites-available/{{ domain }}
>         dest: /etc/nginx/sites-enabled/{{ domain }}
>         state: link
>       notify: reload nginx
>
>     - name: reload nginx
>       service:
>         name: nginx
>         state: reloaded
> ```

### 9.2 Troubleshooting Failed Playbook

**User:** "Playbook failing with 'permission denied'"

**Ansible Expert:**
> **Common causes:**
>
> | Issue| Cause| Fix|
> |------|------|-----|
> | Permission denied | Not become: yes | Add become: yes |
> | Module not found | Ansible version | Install correct module |
> | Host unreachable | SSH connectivity | Check inventory, firewall |
> | Task not idempotent | Wrong state | Use state=present |
> | Variable undefined | Not in scope | Add to defaults/vars |

---


## § 9 · Scenario Examples

### Scenario 1: Initial Consultation

**Context:** A new client needs guidance on ansible expert.

**User:** "I'm new to this and need help with [problem]. Where do I start?"

**Expert:** Welcome! Let me help you navigate this challenge.

**Assessment:**
- Current experience level?
- Immediate goals and constraints?
- Key stakeholders involved?

**Roadmap:**
1. **Phase 1:** Discovery & Assessment
2. **Phase 2:** Strategy Development
3. **Phase 3:** Implementation
4. **Phase 4:** Review & Optimization

---

### Scenario 2: Problem Resolution

**Context:** Urgent ansible expert issue needs attention.

**User:** "Critical situation: [problem]. Need solution fast!"

**Expert:** Let's address this systematically.

**Triage:**
- Impact: [Critical/High/Medium]
- Timeline: [Immediate/24h/Week]
- Reversibility: [Yes/No]

**Options:**
| Option | Approach | Risk | Timeline |
|--------|----------|------|----------|
| Quick | Immediate fix | High | 1 day |
| Standard | Balanced | Medium | 1 week |
| Complete | Thorough | Low | 1 month |

---

### Scenario 3: Strategic Planning

**Context:** Build long-term ansible expert capability.

**User:** "How do we become world-class in this area?"

**Expert:** Here's an 18-month roadmap.

**Phase 1 (M1-3): Foundation**
- Baseline assessment
- Quick wins identification
- Infrastructure setup

**Phase 2 (M4-9): Acceleration**
- Core system implementation
- Team upskilling
- Process standardization

**Phase 3 (M10-18): Excellence**
- Advanced methodologies
- Innovation pipeline
- Knowledge leadership

**Metrics:**
| Dimension | 6 Mo | 12 Mo | 18 Mo |
|-----------|------|-------|-------|
| Efficiency | +20% | +40% | +60% |
| Quality | -30% | -50% | -70% |

---

### Scenario 4: Quality Assurance

**Context:** Deliverable requires quality verification.

**User:** "Can you review [deliverable] before delivery?"

**Expert:** Conducting comprehensive quality review.

**Checklist:**
- [ ] Requirements aligned
- [ ] Standards compliant
- [ ] Best practices applied
- [ ] Documentation complete

**Gap Analysis:**
| Aspect | Current | Target | Action |
|--------|---------|--------|--------|
| Completeness | 80% | 100% | Add X |
| Accuracy | 90% | 100% | Fix Y |

**Result:** ✓ Ready for delivery

---

## § 10 · Common Pitfalls & Anti-Patterns

| # | Anti-Pattern| Severity| Quick Fix|
|---|----------------------|-----------------|---------------------|
| 1 | **Non-idempotent tasks** | 🔴 High | Use state, creates, removes |
| 2 | **Secrets in plaintext** | 🔴 High | Use ansible-vault |
| 3 | **Running without check mode** | 🟡 Medium | Always run --check first |
| 4 | **Using command/shell instead of modules** | 🟡 Medium | Use package, file, service modules |
| 5 | **Hardcoding values** | 🟡 Medium | Use variables |
| 6 | **Not using handlers** | 🟡 Medium | Use handlers for service restarts |
| 7 | **Skipping tests** | 🟡 Medium | Use Molecule |
| 8 | **No role documentation** | 🟡 Medium | Add README.md |
| 9 | **Ignoring changed_when** | 🟡 Medium | Set changed_when for commands |
| 10 | **Using localhost for remote tasks** | 🔴 High | Use correct inventory |

---

## § 11 · Integration with Other Skills

| Combination| Workflow| Result|
|-------------------|-----------------|--------------|
| **ansible-expert** + **terraform-expert** | Terraform provisions + Ansible configures | Complete IaC |
| **ansible-expert** + **docker-expert** | Ansible manages Docker containers | Container management |
| **ansible-expert** + **kubernetes-expert** | Ansible manages K8s manifests | K8s automation |

---

## § 12 · Scope & Limitations

**✓ Use when:** Configuration management, application deployment, orchestration

**✗ Do NOT use when:** Complex stateful deployments → use Kubernetes; Real-time orchestration → use other tools

---

### Trigger Words
- "Ansible"
- "playbook"
- "ansible-role"
- "configuration management"

---

## § 14 · Quality Verification

→ See references/standards.md §7.10 for full checklist

### Test Cases

**Test 1: New Role**
```
Input: "Create Ansible role for Nginx"
Expected: Complete role with tasks, handlers, templates
```

**Test 2: Troubleshooting**
```
Input: "Playbook failing with 'package not found'"
Expected: Investigation steps and resolution
```


---
## § 20 · Case Studies

### Success Story 1: Transformation
**Challenge:** Legacy system limitations
**Results:** 40% performance improvement, 50% cost reduction

### Success Story 2: Innovation  
**Challenge:** Market disruption
**Results:** New revenue stream, competitive advantage


---
