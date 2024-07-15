## 格式化

```go
package main

import "log"

func main() {
	log.SetFlags(log.Ldate | log.Ltime | log.Llongfile)
	log.Fatalln("hello world")
}
```

## zag

```go title="log.go"
package v7

import "go.uber.org/zap"

var sugar *zap.SugaredLogger

func init() {
	logger, _ := zap.NewDevelopment()
	defer logger.Sync() // flushes buffer, if any
	sugar = logger.Sugar()
}

```
json 输出
```go
sugar.Infow("msg","key","val","key1","val1",)
```
