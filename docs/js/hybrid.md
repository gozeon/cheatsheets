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
  iframe.src = url.href
  document.body.appendChild(iframe)
}
```

## 类

固定全局函数

```js

class Hybrid {
  /**
   * 
   * @param protocol "schema:"
   * @param hostname "app.com"
   * @param pathname "/"
   * @param actionMap map
   */
  constructor(protocol, hostname, pathname, actionMap) {
    this.protocol = confg.protocol
    this.protocol = confg.protocol

    this.url = new URL("http://example.com")
    this.url.protocol = protocol
    this.url.hostname = hostname
    this.url.pathname = pathname

    this.actionMap = actionMap
  }

  run({ actionName, params }) {
    return new Promise((resolve, reject) => {
      if (actionName && this.actionMap.has(actionName)) {
        const url = new URL(this.url)
        for (let k in params) {
          url.searchParams.set(k, params[k])
        }

        const funcName = this.actionMap.get(actionName)
        url.searchParams.set('action', actionName)
        url.searchParams.set('callback', funcName)

        window[funcName] = () => resolve(arguments)

        const iframe = document.createElement("iframe")
        iframe.style.display = 'none'
        iframe.src = url.href
        document.body.appendChild(iframe)
      } else {
        reject(`no action: ${actionName}`)
      }
    })
  }
}



```

## 类+callback pool

固定类名字，使每个回调都执行

```js
class Hybrid {
  /**
   * 
   * @param protocol "schema:"
   * @param hostname "app.com"
   * @param pathname "/"
   * @param actionMap map
   */
  constructor(protocol, hostname, pathname, actionMap) {
    this.protocol = confg.protocol
    this.protocol = confg.protocol

    this.url = new URL("http://example.com")
    this.url.protocol = protocol
    this.url.hostname = hostname
    this.url.pathname = pathname

    this.actionMap = actionMap

    this.callback_pool = {}
  }

  run({ actionName, params }) {
    return new Promise((resolve, reject) => {
      if (actionName && this.actionMap.has(actionName)) {
        const traceID = Math.random().toString(36).slice(-5)
        const url = new URL(this.url)
        for (let k in params) {
          url.searchParams.set(k, params[k])
        }

        const funcName = this.actionMap.get(actionName)
        url.searchParams.set('action', actionName)
        url.searchParams.set('callback', funcName)
        url.searchParams.set('_traceID', traceID)

        this.callback_pool[traceID] = () => resolve(arguments)
        window[funcName] = () => {
          this.callback_pool[traceID].call(null, arguments)
          delete this.callback_pool[traceID]
        }

        const iframe = document.createElement("iframe")
        iframe.style.display = 'none'
        iframe.src = url.href
        document.body.appendChild(iframe)
      } else {
        reject(`no action: ${actionName}`)
      }
    })
  }
}


```
