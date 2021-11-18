---
title: css
category: Css
intro: See MDN Web Docs [Css](https://developer.mozilla.org/en-US/docs/Web/CSS)
---

# 常用

### 虚线边框

[参考 1](https://css-tricks.com/more-control-over-css-borders-with-background-image/)
[参考 2](https://www.cnblogs.com/libin-1/p/7096926.html)

```css
.border-dotted {
  padding: 1em;
  border: 1px dashed transparent;
  background: linear-gradient(white, white) padding-box, repeating-linear-gradient(
      -45deg,
      #ccc 0,
      #ccc 0.25em,
      white 0,
      white 0.75em
    );
}
```

### flex 布局

宽高失效问题

```css
/* 
flex-grow: 此属性为是否自动增长空间，
flex-shrink;此属性为是否自动缩小空间，
默认值都是1，即自动增长/缩小，
设置为0时，不会自动增长/缩小
*/
flex-grow: 0;
flex-shrink: 0;
```
