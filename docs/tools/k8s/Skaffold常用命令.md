### 运行应用并构建部署
```
skaffold run
```
### 构建应用
```
skaffold build
```

### 部署应用
```
skaffold deploy
```

### 监视文件变动并自动构建部署
```
skaffold dev
```

### 输出构建信息
```
skaffold build --verbosity debug
```

### 使用指定配置文件
```
skaffold -f skaffold.yaml run
```

### 清除已部署的应用
```
skaffold delete
```

### 查看当前 Skaffold 配置文件的内容
```
skaffold config view
```

### 仅构建但不部署
```
skaffold build --no-deploy
```

### 查看 Skaffold 版本
```
skaffold version
```
