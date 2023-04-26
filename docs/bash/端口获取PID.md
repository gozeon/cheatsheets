## lsof

```bash
# 详细
lsof -i:8080

# 仅pid
lsof -t -i:8080
```

## netstat
```bash
netstat -anp | grep 8080
```
