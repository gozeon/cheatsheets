## 插入 js 内容

babel 编译，插入`script`, see [doc](https://babeljs.io/docs/en/babel-standalone)

```js
var input = 'const getMessage = () => "Hello World";'
var output = Babel.transform(input, { presets: ['env'] }).code
console.log(output)
var script = document.createElement('script')
script.type = 'text/javascript'
try {
  script.appendChild(document.createTextNode(output))
} catch (e) {
  script.text = output
}
document.body.appendChild(script)
```
