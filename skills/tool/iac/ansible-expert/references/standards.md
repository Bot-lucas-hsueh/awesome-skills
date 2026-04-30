# Standards & Reference

## 7.1 Official Documentation

- [Ansible Documentation](https://docs.ansible.com/)
- [Ansible Galaxy](https://galaxy.ansible.com/)
- [Ansible Community](https://www.ansible.com/community)
- [Ansible AWX](https://github.com/ansible/awx)
- [Ansible Collections](https://docs.ansible.com/ansible/latest/collections/index.html)

## 7.2 Inventory Configuration

### Static Inventory

```ini
# inventory/hosts.ini
[webservers]
web1.example.com ansible_host=192.168.1.10
web2.example.com ansible_host=192.168.1.11

[databases]
db1.example.com ansible_host=192.168.1.20
db2.example.com ansible_host=192.168.1.21

[production:children]
webservers
databases
```

### Dynamic Inventory

```yaml
# inventory/ec2.yaml
plugin: amazon.aws.aws_ec2
regions:
  - us-east-1
filters:
  tag:Environment: production
keyed_groups:
  - key: tag.Name
    prefix: tag
```

## 7.3 Playbook Structure

```yaml
---
- name: Common playbook
  hosts: all
  become: yes
  vars:
    app_user: myapp
    app_dir: /opt/myapp
  
  tasks:
    - name: Ensure user exists
      ansible.builtin.user:
        name: "{{ app_user }}"
        state: present
        shell: /bin/bash
    
    - name: Install packages
      ansible.builtin.apt:
        name:
          - nginx
          - python3
          - git
        update_cache: yes
      when: ansible_os_family == "Debian"
    
    - name: Deploy application
      ansible.builtin.git:
        repo: "https://github.com/org/repo.git"
        dest: "{{ app_dir }}"
        version: main
      notify: Restart nginx
  
  handlers:
    - name: Restart nginx
      ansible.builtin.service:
        name: nginx
        state: restarted
```

## 7.4 Module Reference

| Module | Purpose | Example |
|--------|---------|---------|
| `apt` / `yum` | Package management | `apt: name=nginx state=present` |
| `copy` | File copy | `copy: src=file dest=/path` |
| `template` | Template rendering | `template: src=cfg.j2 dest=/path` |
| `service` | Service control | `service: name=nginx state=started` |
| `user` | User management | `user: name=app state=present` |
| `shell` | Shell commands | `shell: rm -rf /tmp/*` |
| `git` | Git operations | `git: repo=url dest=/path` |
| `docker_container` | Docker management | `docker_container: name=app image=nginx` |

## 7.5 Role Structure

```
roles/
├── common/
│   ├── defaults/
│   │   └── main.yml      # Default variables
│   ├── tasks/
│   │   └── main.yml      # Tasks
│   ├── handlers/
│   │   └── main.yml      # Handlers
│   ├── templates/
│   │   └── config.j2     # Jinja2 templates
│   └── vars/
│       └── main.yml      # Role variables
```

## 7.6 Version Compatibility

| Ansible Version | Status | Notes |
|----------------|--------|-------|
| 2.17+ | Current | Latest features |
| 2.16+ | Supported | Recommended |
| 2.15+ | Supported | LTS candidate |
| 2.14+ | Security only | Legacy |
