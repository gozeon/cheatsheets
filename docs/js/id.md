## 生成随机数

https://stackoverflow.com/questions/105034/how-to-create-a-guid-uuid

```js
export const shortId = () => Math.random().toString(36).substring(2) + Date.now().toString(36);
```

## shortId（基本原理）

```js
export const shortId = () =>Math.random().toString(32).slice(2)
```
