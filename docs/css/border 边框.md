## 虚线边框 
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
