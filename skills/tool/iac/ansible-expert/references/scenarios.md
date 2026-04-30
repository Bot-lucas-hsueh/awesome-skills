# Scenario Examples

## 9.1 Web Server Deployment

**User:** "How do I deploy a web server with Ansible?"

**Ansible Expert:**
> **Playbook:**
>
> ```yaml
> ---
> - name: Deploy web server
>   hosts: webservers
>   become: yes
>   
>   vars:
>     nginx_version: "1.24"
>   
>   tasks:
>     - name: Install Nginx
>       ansible.builtin.apt:
>         name: nginx
>         state: present
>         update_cache: yes
>     
>     - name: Configure Nginx
>       ansible.builtin.template:
>         src: nginx.conf.j2
>         dest: /etc/nginx/nginx.conf
>       notify: Reload nginx
>     
>     - name: Deploy application
>       ansible.builtin.git:
>         repo: "{{ app_repo }}"
>         dest: /var/www/app
>         version: "{{ app_version }}"
>     
>     - name: Start Nginx
>       ansible.builtin.service:
>         name: nginx
>         state: started
>         enabled: yes
>   
>   handlers:
>     - name: Reload nginx
>       ansible.builtin.service:
>         name: nginx
>         state: reloaded
> ```
>
> **Template (nginx.conf.j2):**
> ```jinja2
> server {
>     listen {{ nginx_port | default(80) }};
>     server_name {{ server_name }};
>     
>     location / {
>         root {{ app_dir | default('/var/www/app') }};
>         index index.html;
>     }
> }
> ```

## 9.2 Database Setup

**User:** "How do I set up PostgreSQL?"

**Ansible Expert:**
> **Playbook:**
>
> ```yaml
> ---
> - name: Setup PostgreSQL
>   hosts: databases
>   become: yes
>   
>   vars:
>     db_name: myapp
>     db_user: myapp_user
>   
>   tasks:
>     - name: Install PostgreSQL
>       ansible.builtin.apt:
>         name:
>           - postgresql
>           - postgresql-contrib
>           - python3-psycopg2
>         state: present
>     
>     - name: Ensure PostgreSQL is running
>       ansible.builtin.service:
>         name: postgresql
>         state: started
>         enabled: yes
>     
>     - name: Create database
>       community.postgresql.postgresql_db:
>         name: "{{ db_name }}"
>         state: present
>     
>     - name: Create user
>       community.postgresql.postgresql_user:
>         name: "{{ db_user }}"
>         password: "{{ db_password }}"
>         priv: "{{ db_name }}:ALL"
>         state: present
> ```

## 9.3 Docker Deployment

**User:** "How do I deploy a Docker container?"

**Ansible Expert:**
> **Playbook:**
>
> ```yaml
> ---
> - name: Deploy Docker containers
>   hosts: docker_hosts
>   become: yes
>   
>   tasks:
>     - name: Install Docker
>       ansible.builtin.include_role:
>         name: geerlingguy.docker
>     
>     - name: Pull Docker image
>       docker_image:
>         name: "{{ app_image }}"
>         source: pull
>         force_source: yes
>     
>     - name: Create container
>       docker_container:
>         name: "{{ app_name }}"
>         image: "{{ app_image }}"
>         state: started
>         restart_policy: always
>         ports:
>           - "{{ app_port }}:80"
>         env:
>           DATABASE_URL: "{{ db_url }}"
>         volumes:
>           - app_data:/data
> ```
