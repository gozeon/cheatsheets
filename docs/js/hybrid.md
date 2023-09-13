## hybrid 简单例子

动态全局函数

```js
function hybrid({ actionName, params, callback }) {
  const iframe = document.createElement("iframe")

  const url = new URL("http://example.com")
  url.protocol = "schema:"
  url.hostname = "app.com"
  url.pathname = "/"

  for (let k in params) {
    url.searchParams.set(k, params[k])
  }

  const funcName = `action_callback_${Math.random().toString(36).slice(-5)}`
  window[funcName] = function () {
    callback && callback(...arguments)
  }

  url.searchParams.set('action', actionName)
  url.searchParams.set('callback', funcName)

  iframe.style.display = 'none'
  document.appendChild(iframe)
}
```
