---
title: javascript
category: Javascript
intro: See MDN Web Docs [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
---

# Boolean

### boolean

The Boolean object is an object wrapper for a boolean value.

```js
var x = new Boolean(false)
if (x) {
  // this code is executed
}
```

# Array

### asIntN

The BigInt.asIntN static method clamps a BigInt value to a signed integer value, and returns that value.

```
const max = 2n ** (64n - 1n) - 1n;

function check64bit(number) {
  (number > max) ?
    console.log('Number doesn\'t fit in signed 64-bit integer!') :
    console.log(BigInt.asIntN(64, number));
}

check64bit(2n ** 64n);
// expected output: "Number doesn't fit in signed 64-bit integer!"

check64bit(2n ** 32n);
// expected output: 4294967296n
```

### asUintN

The BigInt.asUintN static method clamps a BigInt value to an unsigned integer value, and returns that value.

```
const max = 2n ** 64n - 1n;

function check64bit(number) {
  (number > max) ?
    console.log('Number doesn\'t fit in unsigned 64-bit integer!') :
    console.log(BigInt.asUintN(64, number));
}

check64bit(2n ** 64n);
// expected output: "Number doesn't fit in unsigned 64-bit integer!"

check64bit(2n ** 32n);
// expected output: 4294967296n
```
