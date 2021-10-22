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
