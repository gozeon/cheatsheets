### 基本使用

参考文档 [link](https://www.sitepoint.com/manage-javascript-application-state-mobx/)

```js
var data = mobx.observable({
  a: 1,
})

mobx.autorun(function () {
  console.log('autorun', data.a)
})

data.a = 2
```
