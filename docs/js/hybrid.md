## hybrid 简单例子


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

  window[`action_callback_${Math.random().toString(36).slice(-5)}`] = function () {
    callback(...arguments)
  }

  url.searchParams.set('action', actionName)
  url.searchParams.set('callback', callback)

  iframe.style.display = 'none'
  document.appendChild(iframe)
}

```
