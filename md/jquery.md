---
title: jQuery
category: JavaScript,jQuery
intro: '[官网](https://jquery.com/)'
---

# ajax 请求

### 通用

see [doc](https://learn.jquery.com/ajax/)

```js
$.ajax({
  url: '/xxx',
  data: { ...data },
  type: 'POST',
  contentType: 'application/x-www-form-urlencoded',
  cache: false,
  timeout: 1000 * 1,
  success: function (data) {},
  error: function (err) {},
})
```

# 插件

### 基本写法

see [doc](https://learn.jquery.com/plugins/basic-plugin-creation/)

```js
;(function ($) {
  $.fn.pluginname = function (options) {
    var opts = $.extend({}, $.fn.pluginname.defaults, options)
    // do something
  }
  $.fn.pluginname.defaults = {}
})(jQuery)
```

# When 与 Deferred

### 基本使用

```js
$.when($.ajax('test.aspx')).then(function (data, textStatus, jqXHR) {
  alert(jqXHR.status) // Alerts 200
})
```

### 组合使用

```js
var d1 = $.Deferred()
var d2 = $.Deferred()

$.when(d1, d2).done(function (v1, v2) {
  console.log(v1) // "Fish"
  console.log(v2) // "Pizza"
})

d1.resolve('Fish')
d2.resolve('Pizza')
```

### 请求

```js
function getData() {
  var deferred = $.Deferred()

  $.ajax({
    url: 'http://google.com',
    success: function (data) {
      deferred.resolve('yay')
    },
    error: function (error) {
      deferred.reject('boo')
    },
  })

  return deferred.promise()
}

$.when(getData()).done(function (value) {
  alert(value)
})

getData().then(function (value) {
  alert(value)
})
```
