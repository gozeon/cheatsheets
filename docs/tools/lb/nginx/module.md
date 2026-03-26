
```bash

nginx -V 2>&1 | grep module

[root@storage3 tmp]# nginx -V 2>&1
nginx version: nginx/1.15.7
built by gcc 4.8.5 20150623 (Red Hat 4.8.5-36) (GCC) 
built with OpenSSL 1.1.0j  20 Nov 2018
TLS SNI support enabled
configure arguments: --sbin-path=/usr/local/nginx/nginx --conf-path=/usr/local/nginx/nginx.conf --pid-path=/usr/local/nginx/nginx.pid --with-http_ssl_module --with-http_gzip_static_module --with-pcre=/home/tmp/pcre-8.42 --with-zlib=/home/tmp/zlib-1.2.11 --with-openssl=/home/tmp/openssl-1.1.0j --add-module=/home/tmp/nginx-upload-module-master
```
