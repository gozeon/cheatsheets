---
title: pm2
category: javaScript, nodeJs, other
intro: See  [Docs](https://pm2.keymetrics.io/)
---

# 常用命令

### 基本使用

```npm
pm2 status # 查看所有进程
pm2 log # 查看日志
pm2 show <name/id> # 查看进程详情
pm2 reload <name/id> # 平滑重启进程，
pm2 restart <name/id> --update-env # 重启进程并重新载入环境变量
pm2 ecosystem init # 初始化配置文件
```

# 常用配置文件

### `django`举例

`ecosystem.config.js`

```js
module.exports = {
  apps: [
    {
      name: 'django',
      cwd: '/Users/goze/python/ac',
      args: 'runserver 0.0.0.0:8989',
      script: 'manage.py',
      exec_mode: 'fork',
      exec_interpreter: '/Users/goze/python/ac/env/bin/python',
    },
  ],
}
```

### `nodeJs`举例

```js
module.exports = {
  apps: [
    {
      name: 'xxx',
      script: 'app.js',
      // 机器mem为 20g  11c
      node_args: '--max_old_space_size=2048',
      instances: 'max',
      autorestart: true,
      watch: false,
      // max_memory_restart: '600M',
      env: {
        NODE_ENV: 'development',
      },
      env_production: {
        NODE_ENV: 'production',
      },
    },
  ],
}
```
