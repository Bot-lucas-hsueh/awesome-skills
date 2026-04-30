# yaml Example

```
# roles/nginx/tasks/main.yml
---
- name: Install Nginx
  package:
    name: nginx
    state: present

- name: Create nginx config
  template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
    owner: root
    group: root
    mode: '0644'
    validate: nginx -t -c %s
  notify: reload nginx

- name: Enable site configuration
  template:
    src: site.conf.j2
    dest: "/etc/nginx/sites-available/{{ nginx_site_name }}"
    owner: root
    group: root
    mode: '0644'
  notify: enable site

- name: Start and enable Nginx
  service:
    name: nginx
    state: started
    enabled: yes

# roles/nginx/defaults/main.yml
---
nginx_site_name: default
nginx_port: 80
nginx_server_name: localhost
nginx_root: /var/www/html
```
