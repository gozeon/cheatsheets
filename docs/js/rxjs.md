## 基本使用

参考文档 [link](https://www.learnrxjs.io/learn-rxjs/subjects/behaviorsubject)

```js
// var sub = new rxjs.Subject()
var sub = new rxjs.BehaviorSubject()
sub.next({ a: 1 })
sub.subscribe((x) => {
  console.log('Subscriber A', x)
})
sub.next({ a: 2 })
sub.subscribe((x) => {
  console.log('Subscriber B', x)
  // make sure BehaviorSubject
  console.log(sub.getValue())
})
sub.next(3)

console.log('------------with other api ------------')
const observable = rxjs.interval(500).pipe(rxjs.take(41))
observable.subscribe(sub)
```
