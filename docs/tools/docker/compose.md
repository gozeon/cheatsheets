
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

## 🚀 Lifecycle & Deployment
Command	Action	Key Use Case  
`docker compose up`	Create & start	Standard way to launch your stack.  
`docker compose up -d`	Start detached	Run containers in the background.  
`docker compose stop`	Stop services	Halts processes; keeps containers & data.  
`docker compose start`	Start stopped	Restarts previously stopped containers.  
`docker compose down`	Stop & remove	Clean up everything (containers/networks).  
`docker compose down -v`	Deep cleanup	Removes everything plus named volumes.  
`docker compose restart`	Restart	Quick reboot of a service.  
## 🛠️ Development & Maintenance
Command	Action	Key Use Case  
`docker compose build`	Build images	Update images after changing a Dockerfile.  
`docker compose up` --build	Rebuild & start	Force a fresh build before launching.  
`docker compose rm`	Remove stopped	Delete containers that are already stopped.  
`docker compose pull`	Pull images	Update to the latest image versions from a registry.  
`docker compose config`	Validate	Check your .yml file for syntax errors.  
## 🔍 Monitoring & Debugging
Command	Action	Key Use Case  
`docker compose ps`	List status	See which services are running/exited.  
`docker compose logs`	View logs	See output from all services.  
`docker compose logs -f`	Follow logs	Watch live output/errors as they happen.  
`docker compose top`	List processes	See what's running inside each container.  
`docker compose stats`	Resource usage	Monitor CPU and RAM consumption.  
## ⌨️ Interaction
Command	Action	Key Use Case  
`docker compose exec <svc> <cmd>`	Run in running	Open a shell (e.g., exec web bash).  
`docker compose run <svc> <cmd>`	Run in new	Run one-off tasks (e.g., DB migrations).  

## 🛠️ Service Management Commands
Action	Command	What it actually does  
Stop	`docker compose stop <service>`	Halts the processes; container & data stay.  
Stop All	`docker compose stop`	Stops every service in the .yml file.  
Delete	`docker compose rm -s <service>`	Stops and removes the container.  
Delete All	`docker compose down`	Stops/removes all containers and networks.  
Delete + Data	`docker compose down -v`	Stops/removes everything including volumes.  
Recreate	`docker compose up -d --force-recreate <service>`	Destroys the old container and starts a fresh one.  
Rebuild & Recreate	`docker compose up -d --build <service>`	Rebuilds the image first, then recreates.  
Recreate Clean	`docker compose up -d --no-deps --force-recreate <service>`	Recreates ONLY that service (ignores linked ones).  
