
## 获取最近一次commit hash

> 可作为代码标识或版本，可参考 https://skaffold.dev/docs/taggers/

```bash
git rev-parse --short HEAD
git rev-parse HEAD
git log -1 --pretty=format:"%H"


#  映射为环境变量，方便使用
export GIT_COMMIT=$(git rev-parse --short HEAD)
```

