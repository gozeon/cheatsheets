## 通用

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
