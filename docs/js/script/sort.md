

## 排序

```js title="sort.js"
var arr = [1, 2, 4, 3]
// asc
arr.sort((a, b) => a - b)

var arr = [
    { c: 1 },
    { c: 2 },
    { c: 4 },
    { c: 3 },
]

// asc
arr.sort((a, b) => a.c - b.c)

// https://stackoverflow.com/questions/1129216/sort-array-of-objects-by-string-property-value
// asc
arr.sort((a, b) => {

    if (a.c - b.c > 0) {
        return 1
    }

    if (a.c - b.c < 0) {
        return -1
    }

    return 0
})


```
