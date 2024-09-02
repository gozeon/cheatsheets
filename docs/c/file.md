## 监控文件变化

```c title="main.c"
--8<-- "code/c/file-watch.c"
```

## json 日志格式化

> 使用[jq](https://github.com/jqlang/jq)更方便

`gcc -o jcat main.c -lcjson` then `jcat out.log`

```c title="main.c"
--8<-- "code/c/json-log-print.c"
```
