## 环境判断

```js
const isIos = () => /iPad|iPhone|iPod/i.test(window.navigator.userAgent)
const isAndroid = () => /android/i.test(window.navigator.userAgent)
```
