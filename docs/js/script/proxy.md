
## proxy with node

package version 

```json 
{
    "express": "^4.18.2",
    "http-proxy-middleware": "^2.0.6"
}
```

```js title="main.js"
const express = require('express');
const cors = require('cors')
const { createProxyMiddleware, responseInterceptor } = require('http-proxy-middleware');

const app = express();

app.use(cors())
app.use('/mp4', createProxyMiddleware({ target: 'http://bos.vod.bd.xxxxx.com.cn', changeOrigin: true, pathRewrite: { '^/mp4': '' } }));

app.use('/m3u8', createProxyMiddleware({
    target: 'http://livebackold2.xxxxx.com.cn',
    changeOrigin: true,
    pathRewrite: { '^/m3u8': '' },

    selfHandleResponse: true,
    onProxyRes: responseInterceptor(async (responseBuffer, proxyRes, req, res) => {
        // 302
        if ([302, 307, 308].indexOf(proxyRes.statusCode) > -1 && proxyRes.headers.location) {
            var redirect = proxyRes.headers.location
            redirect = redirect.replace('http://livebackold2.xxxxx.com.cn', 'http://localhost:3000/m3u8')
            res.setHeader('location', redirect)
        }
        const response = responseBuffer.toString('utf8');

        // m3u8 link
        if(/\.m3u8/.test(response)) {
            return response.replace('http://livebackold2.xxxxx.com.cn', 'http://localhost:3000/m3u8')
        }

        return responseBuffer;
    }),
}));

app.listen(3000);
```
