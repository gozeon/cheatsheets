```js
// 基础
layer.msg('hello');

// 标题
layer.open({
  title: 'x',
  content: 'xxxx'
});

// 图标
layer.msg('不开心。。', {icon: 5});

// 询问
layer.confirm('is not?', function(index){
  //do something
  
  layer.close(index);
});  
```
