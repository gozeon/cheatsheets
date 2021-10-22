---
title: nginx
category: nginx,other
intro: '[官网](https://www.nginx.com/)'
---

# 常用配置

### 静态目录

将目录作为静态文件服务器

```nginx
server {
    listen       80 default_server;
    listen       [::]:80 default_server;
    server_name  _;
    # root         /usr/share/nginx/html;

    # Load configuration files for the default server block.
    include /etc/nginx/default.d/*.conf;

    location / {
        root /root;

        autoindex on;
        autoindex_exact_size on;
        autoindex_localtime on;
    }

    error_page 404 /404.html;
        location = /40x.html {
    }

    error_page 500 502 503 504 /50x.html;
        location = /50x.html {
    }

}
```

### 基本转发

转发前端资源和后端服务，前端资源为统一目录，毋需修改配置

```nginx
server {
    listen       80;
    listen       [::]:80;
    server_name  _;
    #root         /usr/share/nginx/html;

    # Load configuration files for the default server block.
    include /etc/nginx/default.d/*.conf;

	location ~ ^/(static)/ {
           root /home/homework/webroot;
        }
        location ~ \.html$ {
           root /home/homework/webroot;
        }
        location ~* ^/+workflow/.* {
           proxy_pass http://127.0.0.1:8080;
        }

        error_page 404 /404.html;
        location = /404.html {
        }

        error_page 500 502 503 504 /50x.html;
        location = /50x.html {
        }
    }
}
```
