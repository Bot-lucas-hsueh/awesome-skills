# Troubleshooting Guide

## 8.1 Playbook Issues

### SSH Connection Failed
```bash
# Test connection
ansible all -m ping

# Debug mode
ansible all -m ping -vvv

# Check inventory
ansible-inventory --list
```

### Permission Denied
- Use `-b` for become (sudo)
- Check ansible_user exists
- Verify sudo NOPASSWD configured

## 8.2 Module Failures

### Module Not Found
- Install collection: `ansible-galaxy collection install community.general`
- Use correct FQCN: `ansible.builtin.yum`

### Task Failed
- Check with `--check` flag
- Use `ignore_errors: yes` temporarily
- Review error message

## 8.3 Inventory Issues

### Host Not Found
- Verify inventory file format
- Check hosts.yaml vs hosts.ini
- Use `ansible-inventory -i inventory.yml --list`

## 8.4 Variable Issues

### Undefined Variable
- Add `default` filter: `{{ variable | default('value') }}`
- Use `vars_files` for variables
- Check group_vars/all

## 8.5 Performance Issues

### Slow Execution
```ini
# ansible.cfg
[pdefaults]
gathering = explicit
forks = 50
```

## 8.6 Debug Commands

```bash
# Syntax check
ansible-playbook --syntax-check playbook.yml

# List tasks
ansible-playbook playbook.yml --list-tasks

# Start at specific task
ansible-playbook playbook.yml --start-at-task="task name"
```