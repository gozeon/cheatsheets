### 安装 Helm Chart
```
helm install <release-name> <chart-name>
```

### 安装时指定配置文件
```
helm install <release-name> <chart-name> -f values.yaml
```

### 升级已有的 Release
```
helm upgrade <release-name> <chart-name>
```

### 卸载已安装的 Release
```
helm uninstall <release-name>
```

### 查看已安装的 Helm Release
```
helm list
```

### 查看指定 Release 的详细信息
```
helm status <release-name>
```

### 查看 Helm Chart 的模板
```
helm template <chart-name>
```

### 搜索 Helm Chart
```
helm search repo <chart-name>
```

### 查看 Helm Chart 版本
```
helm show chart <chart-name>
```

### 获取已安装 Release 的历史记录
```
helm history <release-name>
```

### 回滚 Release 到指定版本
```
helm rollback <release-name> <revision-number>
```

### 查看 Helm 版本
```
helm version
```

### 在安装时设置 Helm 参数
```
helm install <release-name> <chart-name> --set key=value
```
