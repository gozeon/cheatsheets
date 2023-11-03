
## ios环境，详情页返回列表页，tab消失

```js
onMounted(() => {
 nextTick(() => {
  document?.scrollingElement.scrollTop = 0
 })
})
```

相关链接  
- [https://github.com/youzan/vant/issues/10550](https://github.com/youzan/vant/issues/10550)
- [https://blog.csdn.net/weixin_48286936/article/details/122999331](https://blog.csdn.net/weixin_48286936/article/details/122999331)
- [https://www.zhangxinxu.com/wordpress/2019/02/document-scrollingelement/comment-page-1/
](https://www.zhangxinxu.com/wordpress/2019/02/document-scrollingelement/comment-page-1/
)
