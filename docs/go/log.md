## 格式化

```go
package main

import "log"

func main() {
	log.SetFlags(log.Ldate | log.Ltime | log.Llongfile)
	log.Fatalln("hello world")
}
```
