---
title: bash
category: Bash
intro: See [Docs](https://www.gnu.org/software/bash/)
---

# 常用脚本

### 上传文件

上传文件到服务器目录，自动输入密码

```bash
#!/usr/bin/expect -f

# 增加权限
# chmod +x scp.sh
# 执行
# ./scp.sh

# 本地目录 ./dist
spawn bash -c "scp -r ./dist root@IP:/var/www/html"

expect {
  -re ".*es.*o.*" {
    exp_send "yes\r"
    exp_continue
  }
  -re ".*sword.*" {
    exp_send "PASSWORD\r"
  }
}
interact
```

### zip 压缩

遍历目录，将目录压缩成 zip，文件名为目录名

```bash
#!/bin/bash

###
# 描述：遍历目录，将文件夹打包成zip，上传cms
# 运行：sh zip.sh
# 环境：需支持bash和zip命令
###

# verbose 日志
set -ex

cwd=`pwd`

for file in `ls $cwd`
do
    if [ -d $cwd"/"$file ] ;then
        cd $file
        # -x 排除文件
        zip $file.zip -r ./* -x '*.zip*'
        # 如果将zip包移动出来，也可以不移动出来
        mv $file.zip ../
        cd ..
    fi
done

```
