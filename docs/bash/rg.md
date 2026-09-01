

https://github.com/BurntSushi/ripgrep

```bash
rg "hello"

rg "hello" src/

 rg "rec.wisetv" /etc /home /var /usr/local # 多目录

rg "hello" -C 3   #显示3行

rg "hello" --hidden #包含隐藏文件

rg "hello" -uu #包含隐藏文件+屏蔽ignore文件
```

## 可执行文件

> 下载musl完全静态版
> 芯片架构注意： `uname -m`输出 x86_64 表示 Intel/AMD 64位架构；输出 aarch64 表示 ARM 64位架构(华为鲲鹏)

https://github.com/BurntSushi/ripgrep/releases/download/15.2.0/ripgrep-15.2.0-x86_64-unknown-linux-musl.tar.gz
