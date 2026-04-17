# Common Pitfalls & Anti-Patterns

## 10.1 Common Mistakes

| # | Mistake | Severity | Prevention |
|---|---------|----------|------------|
| 1 | Not using check mode | 🔴 High | Always `--check` before apply |
| 2 | Using `shell` instead of modules | 🔴 High | Prefer dedicated modules |
| 3 | Not idempotent tasks | 🔴 High | Design for re-runnability |
| 4 | Hardcoding secrets | 🔴 High | Use Ansible Vault |
| 5 | Ignoring changed_when | 🟡 Medium | Set proper change detection |
| 6 | Not using tags | 🟡 Medium | Enable selective execution |

## 10.2 Anti-Patterns

### Shell vs Modules

```yaml
# BAD: Using shell
- name: Install package
  shell: apt-get install -y nginx

# GOOD: Using apt module
- name: Install package
  apt:
    name: nginx
    state: present
```

### Password Security

```yaml
# BAD: Plain text password
- name: Create user
  user:
    name: app
    password: "secret123"

# GOOD: Encrypted password
- name: Create user
  user:
    name: app
    password: "{{ vault_app_password }}"

# In vault file:
# vault_app_password: "encrypted_value"
```

## 10.3 Performance Anti-Patterns

| Anti-Pattern | Solution |
|--------------|----------|
| Serial execution | Use `strategy: free` |
| No pipelining | Enable `pipelining=True` in ansible.cfg |
| Not using fact caching | Enable `gathering=smart fact_caching=redis` |

## 10.4 Best Practices

```
Playbooks:
□ Use roles for organization
□ Keep playbooks short
□ Use tags for selective runs
□ Handle failures gracefully

Variables:
□ Use meaningful names
□ Scope appropriately (host/group/role)
□ Document variables
□ Use Vault for secrets

Tasks:
□ Use modules over shell
□ Idempotent by design
□ Check mode compatible
□ Descriptive names
```
