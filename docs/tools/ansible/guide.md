## ansible

https://linuxhandbook.com/ansible-ad-hoc/

### ssh免密登录

> 最好使用常用镜像，alpine会出现各种错误

```bash
ssh-keygen
sssh-copy-id root@10.0.2.4
sssh-copy-id root@10.0.2.5
sssh-copy-id root@10.0.2.6
```

### 列出所有host

```text title="inventory.ini"
10.0.2.4
10.0.2.5
10.0.2.6
```

找出所有

```bash
ansible all -i inventory.ini --list-hosts
```

### 区分环境

```text title="inventory-env.ini"
[test]
10.0.2.4

[prod]
10.0.2.5
10.0.2.6
```

找出prod

```bash
ansible prod -i inventory-env.ini --list-hosts
```

### 执行简单命令

```
ansible all -i inventory.ini -m raw -a "cat /etc/os-release"
```

### 使用 playbooks

```yaml title="playbook.yml"
- name: first play
  hosts: all
  tasks: 
    - name: create a new file
      file:
        path: /tmp/foo.conf
        mode: 0664
        owner: root
        state: touch
```

```bash
ansible-playbook -i inventory.ini playbook.yml
ansible all -i inventory.ini -m command -a "ls -l /tmp/foo.conf"

# 检查语法
ansible-playbook -i inventory.ini --syntax-check playbook.yml
# 检查机器
ansible-playbook -i inventory.ini --check playbook.yml
```

单独指定机器

```yaml title="playbook.yml"
- name: first play
  hosts: all
  tasks:
    - name: install tmux
      package:
        name: tmux
        state: present
    
    - name: create an archive
      archive:
        path: /var/log
        dest: /tmp/logs.tar.gz
        format: gz

- name: second play
  hosts: 10.0.2.9
  tasks:
    - name: install git
      apt:
        name: git
        state: present
```

指定tag `--tags git` 仅执行tags任务

```yaml title="playbook.yml"
- name: first play
  hosts: all
  tasks:
    - name: install tmux
      package:
        name: tmux
        state: present
    
    - name: create an archive
      archive:
        path: /var/log
        dest: /tmp/logs.tar.gz
        format: gz

- name: second play
  hosts: 10.0.2.9
  tasks:
    - name: install git
      apt:
        name: git
        state: present
      tags: git
```
