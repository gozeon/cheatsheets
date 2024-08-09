## pssh

批量ssh，感觉效果不好

- Parallel ssh (parallel-ssh, upstream calls it pssh), executes commands on
    multiple hosts in parallel
- Parallel scp (parallel-scp, upstream calls it pscp), copies files to
    multiple remote hosts in parallel
- Parallel rsync (parallel-rsync, upstream calls it prsync), efficiently
    copies files to multiple hosts in parallel
- Parallel nuke (parallel-nuke, upstream calls it pnuke), kills processes on
    multiple remote hosts in parallel
- Parallel slurp (parallel-slurp, upstream calls it pslurp), copies files
    from multiple remote hosts to a central host in parallel



```txt title="host.txt"
10.0.2.5
10.0.2.6
10.0.2.7
```

### 传输文件
```bash
parallel-scp -h host.txt -l root ./main /root/main
```

### bash执行
```bash
parallel-ssh -h host.txt -l root "nohup /root/main > /dev/null 2>&1 &"
```

### 杀死进程
```bash
parallel-nuke -v -h ./host.txt -l root main
```
