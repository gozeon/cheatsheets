---
title: js
category: JavaScript, web
intro: See MDN Web [Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
---

# 常用

### 效果库

html+css 效果

```text
背景视频
https://github.com/rishabhp/bideo.js

弹窗
https://github.com/robinparisi/tingle


输入框输入效果
https://github.com/luisvinicius167/ityped


滚动效果 动画
https://github.com/michalsnik/aos
https://github.com/alexfoxy/lax.js

jquery hover 效果
https://github.com/gijsroge/tilt.js

slider
https://github.com/glidejs/glide

popup
https://github.com/sweetalert2/sweetalert2
https://github.com/popperjs/popper-core

progress bar
https://github.com/CodeByZach/pace

notifications
https://carlosroso.com/notyf/

树组件
http://wwwendt.de/tech/fancytree/demo/

滚动条
http://grsmto.github.io/simplebar/

布局+筛选+排序
https://isotope.metafizzy.co/

```

### 插入 js 内容

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
