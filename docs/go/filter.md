## xorfilter

https://github.com/FastFilter/xorfilter  


```go title="main.go"

package main

import (
	"fmt"

	"github.com/FastFilter/xorfilter"
	"github.com/cespare/xxhash/v2"
)

// https://github.com/matrixorigin/matrixone/blob/6ed78f51b8769898a79b07de2593879eec488ff6/pkg/vm/engine/tae/index/filter.go#L58
func hashV1(v []byte) uint64 {
	return xxhash.Sum64(v)
}

func main() {
	item1 := hashV1([]byte("item1"))
	item2 := hashV1([]byte("item2"))
	item3 := hashV1([]byte("item3"))
	item4 := hashV1([]byte("item4"))

	arr := []uint64{item1, item2, item3, item1, item2, item3}
	filter, err := xorfilter.PopulateBinaryFuse8(arr)
	if err != nil {
		fmt.Println(nil)
	}

	fmt.Println(filter.Contains(item1))
	fmt.Println(filter.Contains(item2))
	fmt.Println(filter.Contains(item3))
	fmt.Println(filter.Contains(item4))
}

```
