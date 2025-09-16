## 集群信息
### 查看当前上下文
```
kubectl config current-context
```
### 查看所有上下文
```
kubectl config get-contexts
```
### 切换上下文
```
kubectl config use-context <context-name>
```
### 查看集群节点
```
kubectl get nodes -o wide
```
### 查看集群版本
```
kubectl version
```
---

## 命名空间
### 查看命名空间
```
kubectl get namespaces
```
### 创建命名空间
```
kubectl create namespace <namespace>
```
### 删除命名空间
```
kubectl delete namespace <namespace>
```
### 指定命名空间操作
```
kubectl get pods -n <namespace>
```
---

## Pods 管理
# 查看 Pod 列表
```
kubectl get pods
kubectl get pods -o wide
```
### 查看 Pod 详细信息
```
kubectl describe pod <pod-name>
```
### 查看 Pod 日志
```
kubectl logs <pod-name>
kubectl logs -f <pod-name>                  # 实时跟踪
kubectl logs <pod-name> -c <container-name> # 多容器 Pod
```
### 进入 Pod 交互式终端
```
kubectl exec -it <pod-name> -- /bin/bash
kubectl exec -it <pod-name> -- /bin/sh
```
### 删除 Pod
```
kubectl delete pod <pod-name>
```
---

## Deployment / ReplicaSet
### 查看 Deployment
```
kubectl get deployments
kubectl get deployment <deployment-name> -o yaml
```
### 创建 / 更新 Deployment
```
kubectl apply -f deployment.yaml
kubectl set image deployment/<deployment-name> <container>=<image>:<tag>
kubectl rollout restart deployment/<deployment-name>
```
### 查看 Deployment 状态
```
kubectl rollout status deployment/<deployment-name>
```

### 回滚 Deployment
```
kubectl rollout undo deployment/<deployment-name>
```
### 删除 Deployment
```
kubectl delete deployment <deployment-name>
```
---

## Service
### 查看 Service
```
kubectl get svc
kubectl describe svc <service-name>
```
### 创建 Service
```
kubectl apply -f service.yaml
```
### 删除 Service
```
kubectl delete svc <service-name>
```
---

## ConfigMap / Secret
### 查看 ConfigMap / Secret
```
kubectl get configmap
kubectl get secret
```
### 创建 ConfigMap
```
kubectl create configmap <name> --from-file=<file> --from-literal=key=value
kubectl apply -f configmap.yaml
```
### 创建 Secret
```
kubectl create secret generic <name> --from-literal=key=value
kubectl apply -f secret.yaml
```
---

## 资源监控
### 查看 Pod / Node 资源使用
```
kubectl top pod
kubectl top pod -n <namespace>
kubectl top node
```
### 查看事件
```
kubectl get events --sort-by=.metadata.creationTimestamp
```
---

## 文件操作
### 创建资源
```
kubectl apply -f <file.yaml>
```
### 删除资源
```
kubectl delete -f <file.yaml>
```
### 获取资源 YAML/JSON
```
kubectl get <resource> <name> -o yaml
kubectl get <resource> <name> -o json
```
---

## 常用调试命令
### 检查 Pod 端口映射
```
kubectl port-forward <pod-name> <local-port>:<container-port>
```
### 进入容器调试网络
```
kubectl exec -it <pod-name> -- /bin/bash
```
### 测试服务连通性
```
kubectl run curlpod --image=radial/busyboxplus:curl -i --tty
```

