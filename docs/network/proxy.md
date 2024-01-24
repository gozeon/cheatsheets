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

### 示例

```json title="config.json"
{
  "log": {
    "loglevel": "warning"
  },
  "routing": {
    "domainStrategy": "AsIs",
    "rules": [
      {
        "type": "field",
        "ip": ["geoip:private"],
        "outboundTag": "direct"
      }
    ]
  },
  "inbounds": [
    {
      "listen": "127.0.0.1",
      "port": "2023",
      "protocol": "socks",
      "settings": {
        "auth": "noauth",
        "udp": true,
        "ip": "127.0.0.1"
      }
    }
  ],
  "outbounds": [
    {
      "protocol": "vmess",
      "settings": {
        "vnext": [
          {

            "address": "<xx.xx.xx.xx>",
            "port": 80,
            "users": [
              {
                "id": "<xxx-xx-xx-xx-xx>"
              }
            ]
          }
        ]
      },
      "streamSettings": {
        "network": "ws",
        "wsSettings": {
          "host": "<xx.xx.xx.xx>",
          "path": "</wp-login?ed=2048>"
        }
      },
      "tag": "proxy"
    }
  ]
}

```

## sing-box

https://github.com/SagerNet/sing-box

### 运行

```bash
sing-box run -c config.json
```

### 示例

```json title="config.json"
{
  "log": {
    "disabled": false,
    "level": "info",
    "timestamp": true
  },
  "dns": {},
  "ntp": {},
  "outbounds": [
    {
      "type": "vmess",
      "tag": "vmess-out",
      "server": "<xx.xx.xx.xx>",
      "server_port": 80,
      "uuid": "<xxxx-xxx-xx-xx-xxx>",
      "security": "auto",
      "alter_id": 0,
      "global_padding": false,
      "authenticated_length": true,
      "network": "tcp",
      "tls": {},
      "multiplex": {},
      "transport": {
        "type": "ws",
        "path": "</wp-login?ed=2048>",
        "headers": {
          "host": "<xxx.xxx.xxx>"
        }
      }
    }
  ],
  "inbounds": [
    {
      "type": "mixed",
      "tag": "mixed-in",
      "listen": "::",
      "listen_port": 2024,
      "tcp_fast_open": false,
      "tcp_multi_path": false,
      "udp_fragment": false,
      "udp_timeout": "5m"
    }
  ],
  "route": {
    "rules": [
      {
        "geosite": ["cn"],
        "geoip": ["cn"],
        "outbound": "direct"
      }
    ]
  },
  "experimental": {}
}

```
