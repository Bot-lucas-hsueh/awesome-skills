# yaml Example

```
---
- name: Common Server Configuration
  hosts: webservers
  become: yes
  vars:
    ntp_server: pool.ntp.org
  
  tasks:
    - name: Update apt cache
      apt:
        update_cache: yes
        cache_valid_time: 3600
      when: ansible_os_family == "Debian"
    
    - name: Install common packages
      package:
        name:
          - vim
          - curl
          - git
        state: present
    
    - name: Configure NTP
      template:
        src: ntp.conf.j2
        dest: /etc/ntp.conf
        owner: root
        group: root
        mode: '0644'
      notify: restart ntp
    
    - name: Start and enable services
      service:
        name: "{{ item }}"
        state: started
        enabled: yes
      loop:
        - nginx
        - fail2ban

  handlers:
    - name: restart ntp
      service:
        name: ntp
        state: restarted
```
