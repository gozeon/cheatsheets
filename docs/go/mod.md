## 设置中国镜像

```bash
go env -w GO111MODULE=on
go env -w GOPROXY=https://goproxy.cn,direct
```


## 升级所有包

```bash
go get -u
```


## 参考链接

- https://goproxy.cn/
- https://go.dev/ref/mod

