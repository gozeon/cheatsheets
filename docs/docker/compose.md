
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



## 使用traefix代替nginx

使用[traefix](https://doc.traefik.io/traefik/)，在扩容部署的时候，就不用重启步骤

> 注意使用 --no-deps

```yaml title="docker-compose.yml"
version: '3'

services:

  api:
    build: .
    depends_on:
      - traefik
    labels:
      - "traefik.http.routers.api.rule=Host(`api.docker.localhost`)"

  whoami:
    # A container that exposes an API to show its IP address
    image: traefik/whoami
    labels:
      - "traefik.http.routers.whoami.rule=Host(`whoami.docker.localhost`)"

  traefik:
    # The official v2 Traefik docker image
    image: traefik:v2.10
    # Enables the web UI and tells Traefik to listen to docker
    command: --api.insecure=true --providers.docker
    ports:
      # The HTTP port
      - "80:80"
      # The Web UI (enabled by --api.insecure=true)
      - "8080:8080"
    volumes:
      # So that Traefik can listen to the Docker events
      - /var/run/docker.sock:/var/run/docker.sock

```
