

## 格式化数据，将扁平化数据树形化

- [参考 link 1](https://stackoverflow.com/questions/62938888/nest-flat-objects-based-on-a-parentid-and-id-property)
- [参考 link 2](https://www.w3resource.com/javascript-exercises/fundamental/javascript-fundamental-exercise-90.php)

```js title="nest.js"
function nested(data, pid = undefined) {
  return data.reduce((r, e) => {
    if (e.parentId == pid) {
      const obj = { ...e }
      const children = nested(data, e.id);
      if (children.length) obj.children = children;
      r.push(obj)
    }

    return r;
  }, [])
}
```
