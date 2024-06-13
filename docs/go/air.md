## air 特殊配置

`docker` 环境内一定需要打开 `poll`  

```bash
air --build.cmd "go build -o ../tmp/main main.go" --build.bin "../tmp/main" --build.poll true
```

### 参考
- https://github.com/air-verse/air
- https://stackoverflow.com/questions/70321633/hot-reload-not-working-in-docker-with-golang-github-com-cosmtrek-air/77248470#77248470
