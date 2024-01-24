## 基本使用

```js
laydate.render({
  elem: '#signAt',
  type: 'datetime',
  theme: '#4996ed',
  format: 'yyyy-MM-dd HH:mm:ss',
  done: function () {
    // do somethins
  },
})
```

## 区间

```js
// 单dom
laydate.render({
  elem: '#signAt',
  type: 'datetime',
  theme: '#4996ed',
  range: true, //或 range: '~' 来自定义分割字符
  format: 'yyyy-MM-dd HH:mm:ss',
  done: function () {
    // do somethins
  },
})

// 双dom
laydate.render({
  elem: '#test-range', //开始时间和结束时间所在 input 框的父选择器
  //设置开始日期、日期日期的 input 选择器
  range: ['#startDate', '#endDate'], //数组格式为 layui 2.6.6 开始新增
})
```
