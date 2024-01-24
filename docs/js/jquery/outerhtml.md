
see [link](https://stackoverflow.com/questions/5744207/jquery-outer-html) [link 1](https://www.techiedelight.com/get-outerhtml-element-javascript/)

```js
$('#xxx').prop('outerHTML')
```

or

```js
$('<div>').append($('#xxx').clone()).html();
```
