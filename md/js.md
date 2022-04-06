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

### mobx.js js 例子

参考文档[link](https://www.sitepoint.com/manage-javascript-application-state-mobx/)

```js
var data = mobx.observable({
  a: 1,
})

mobx.autorun(function () {
  console.log('autorun', data.a)
})

data.a = 2
```

### rxjs 例子

参考文档[link](https://www.learnrxjs.io/learn-rxjs/subjects/behaviorsubject)

```js
// var sub = new rxjs.Subject()
var sub = new rxjs.BehaviorSubject()
sub.next({ a: 1 })
sub.subscribe((x) => {
  console.log('Subscriber A', x)
})
sub.next({ a: 2 })
sub.subscribe((x) => {
  console.log('Subscriber B', x)
  // make sure BehaviorSubject
  console.log(sub.getValue())
})
sub.next(3)

console.log('------------with other api ------------')
const observable = rxjs.interval(500).pipe(rxjs.take(41))
observable.subscribe(sub)
```

### js nest , 对象数组转换树结构

可参考[link](https://stackoverflow.com/questions/62938888/nest-flat-objects-based-on-a-parentid-and-id-property), [link2](https://stackoverflow.com/questions/68330014/flat-array-to-tree-javascript)

```js
   { id: 1, parentId: 0, child: [] },
   { id: 2, parentId: 0, child: [] },
   { id: 3, parentId: 1, child: [] },
   { id: 4, parentId: 2, child: [] },
   { id: 5, parentId: 3, child: [] },
   { id: 6, parentId: 4, child: [] },
   { id: 7, parentId: 5, child: [] },
   { id: 8, parentId: 6, child: [] },
]

function nest(data, parentId=0) {
    const result = []

    for(let i = 0; i< data.length; i++) {

        if(data[i].parentId == parentId) {
            result.push(data[i])
            data[i].child = data.filter(item => item.parentId == data[i].id).map(item => {
                item.child = nest(data, item.id)
                return item
            })
        }
    }

    return result
}

console.log(JSON.stringify(nest(data), null, 2))
```
