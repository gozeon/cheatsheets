

https://colobu.com/2021/01/17/go-embed-tutorial/

https://blog.jetbrains.com/go/2021/06/09/how-to-use-go-embed-in-go-1-16/

## 字符串文件

```go
package main
import (
	_ "embed"
	"fmt"
)
//go:embed hello.txt
var s string
func main() {
	fmt.Println(s)
}
```

## 文件夹

```go
package main
import (
	"embed"
	"fmt"
)
//go:embed p
var f embed.FS
func main() {
	data, _ := f.ReadFile("p/hello.txt")
	fmt.Println(string(data))
	data, _ = f.ReadFile("p/hello2.txt")
	fmt.Println(string(data))
}
```
