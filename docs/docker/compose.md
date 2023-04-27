
参考代码 [dockercompose](https://github.com/gozeon/code-collections/tree/master/dockercompose)

## 启动

```bash
docker compose up
```

## 重新编译启动

```bash
docker compose up --build
```

## 扩充节点

```bash
# 会有downtime，因为nginx 会 recreate
docker compose up -d --scale api=10

# 0 downtime 
docker compose up -d --scale api=10 --no-recreate nginx 
# 这种方式需要重启nginx
docker compose exec nginx /usr/sbin/nginx -s reload
```
