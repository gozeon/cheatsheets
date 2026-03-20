

https://github.com/geosigno/simpleParallax.js/  
https://dev.to/ingosteinke/pure-css-parallax-perspective-beyond-landscape-images-24g2

```css
background-attachment: fixed;
```

or

```css
img {
  aspect-ratio: 16 / 9;
  object-fit: cover;
  animation: --parallax linear both;
  animation-timeline: view();
}
@keyframes --parallax {
  from {
    object-position: 0 100%;
  }
  to {
    object-position: 0 0;
  }
}
```
