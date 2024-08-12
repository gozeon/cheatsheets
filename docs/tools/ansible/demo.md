## 部署一个可执行文件

```ini title="inventory.ini"
[alpine]
10.0.2.4
10.0.2.5
10.0.2.6
[ubuntu]
10.0.2.9
10.0.2.8
[tips]
10.0.2.9
[prod]
10.0.2.9
```

```yaml title="deploy.yml"
- hosts: tips
  become: yes
  roles:
    - { role: ansistrano.deploy }
  vars:
    ansistrano_deploy_to: /var/www/your_app
    ansistrano_deploy_via: copy
    ansistrano_deploy_from: /root/my-app
    ansistrano_after_update_code_tasks_file: "{{ playbook_dir }}/hook/after-update-code-tasks.yml"
    ansistrano_after_cleanup_tasks_file: "{{ playbook_dir }}/hook/after-cleanup-tasks.yml"

```

```yaml title="rollback.yml"
- hosts: tips
  become: yes
  roles:
    - { role: ansistrano.rollback }
  vars:
    ansistrano_deploy_to: /var/www/your_app
    ansistrano_rollback_after_cleanup_tasks_file: "{{ playbook_dir }}/hook/after-cleanup-tasks.yml"
```

```yaml title="hook/after-update-code-tasks.yml"
- name: Change file mode
  ansible.builtin.file:
    path: "{{ ansistrano_release_path.stdout }}/my-app/main"
    mode: '0755'
```

```yaml title="hook/after-cleanup-tasks.yml"
- name: close app
  shell: pkill -f {{ ansistrano_deploy_to }}/{{ ansistrano_current_dir }}/my-app/main || /bin/true
  ignore_errors: true
- name: run app
  shell: nohup {{ ansistrano_deploy_to }}/{{ ansistrano_current_dir }}/my-app/main > /dev/null 2>&1 &

```

> -vvv 参数
### 执行

```bash
ansible-playbook -i inventory.ini deploy.yml 
```

### 回滚
```
ansible-playbook -i inventory.ini rollback.yml
```
