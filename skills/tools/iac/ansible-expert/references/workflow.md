# Standard Workflow

## 8.1 Project Setup

```
Phase 1: Initialize
├── Create directory structure
├── Initialize Git repository
├── Create ansible.cfg
└── Set up inventory

Phase 2: Configuration
├── Define inventory (hosts)
├── Create group_vars/all
├── Set up vault for secrets
└── Configure ansible.cfg

Phase 3: Role Development
├── Create roles directory
├── Scaffold role structure
├── Implement tasks
├── Create templates
└── Add handlers

Phase 4: Testing
├── Syntax check: ansible-playbook --syntax-check
├── Dry run: ansible-playbook --check
├── Test in dev environment
└── Run with tags
```

## 8.2 Playbook Execution

```bash
# Syntax check
ansible-playbook -i inventory site.yml --syntax-check

# Dry run
ansible-playbook -i inventory site.yml --check

# Run specific tags
ansible-playbook -i inventory site.yml --tags "nginx,deploy"

# Run with vault
ansible-playbook -i inventory site.yml --ask-vault-pass

# Limit to specific hosts
ansible-playbook -i inventory site.yml --limit webserver1
```

## 8.3 Role Development

```bash
# Create role structure
ansible-galaxy init roles/nginx

# Install from Galaxy
ansible-galaxy install -r requirements.yml

# requirements.yml
---
roles:
  - name: nginx
    version: v1.2.0
collections:
  - name: community.general
```

## 8.4 Testing Workflow

```bash
# Molecule testing
molecule create
molecule converge
molecule verify
molecule destroy

# CI/CD integration
ansible-lint playbook.yml
ansible-playbook --check playbook.yml
```
