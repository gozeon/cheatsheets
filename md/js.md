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

时间
https://github.com/flatpickr/flatpickr

数字效果
https://inorganik.github.io/countUp.js/

滚动效果 动画
https://github.com/michalsnik/aos
https://github.com/alexfoxy/lax.js
https://github.com/silvestreh/onScreen

jquery hover 效果
https://github.com/gijsroge/tilt.js

slider
https://github.com/glidejs/glide
https://refreshless.com/nouislider/

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

select
https://choices-js.github.io/Choices/
https://select2.org

数字处理
https://mathjs.org/index.html
http://numeraljs.com/

校验
https://github.com/yiminghe/async-validator
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

### Cleave.js 百分比例子

[Cleave.js](https://github.com/nosir/cleave.js)

```js
var cleave = new Cleave('.input-phone', {
  numeral: true,
  prefix: '%',
  tailPrefix: true,
  noImmediatePrefix: true,
  numericOnly: true,
  // numeralDecimalScale: 0,
  onValueChanged: function (ee) {
    console.log(ee.target)
  },
})

// 设置值
cleave.setRawValue('123')

// 获取值
cleave.getRawValue()
```
