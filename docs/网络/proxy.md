## v2ray or xray 

### 运行

```bash
v2ray run -c config.json
```

### 配置

参考[配置例子](https://github.com/XTLS/Xray-examples),  [transport-settings](https://www.v2ray.com/en/configuration/transport.html#transport-settings)

```title="内部配置"
...
"streamSettings": {
  "network": "ws",
  "wsSettings": {
    "host": "xxxx",
    "path": "/xxxx?ed=2048"
  }
},

...
```
