[doc](https://github.com/nosir/cleave.js)

## 百分比例子

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
