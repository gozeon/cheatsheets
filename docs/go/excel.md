
## 按行写入

http://liuqh.icu/2021/06/30/go/package/21-excelize/

```go title="insertRow.go"
package main

import (
	"fmt"
	"strconv"

	"github.com/xuri/excelize/v2"
)

func main() {
	f := excelize.NewFile()

	headers := []interface{}{"index", "count", "date"}
	f.SetSheetRow("Sheet1", "A1", &headers)

	values := []interface{}{
		[]interface{}{"1", 2, "2022/01/01"},
		[]interface{}{"2", 3, "2022/02/01"},
	}

	for i, v := range values {
		tmp, _ := v.([]interface{})
		err := f.SetSheetRow("Sheet1", "A"+strconv.Itoa(i+2), &tmp)
		if err != nil {
			fmt.Println(err)
		}
	}

	if err := f.SaveAs("Book1.xlsx"); err != nil {
		fmt.Println(err)
	}
}

```
