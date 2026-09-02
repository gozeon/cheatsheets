go build 是 Go 语言用于编译源码并生成可执行二进制文件的核心命令。

## 示例命令解析
`CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build` 这条命令常用于在 macOS 或 Windows 等非 Linux 开发机上，交叉编译出能在 Linux 服务器上独立运行的二进制文件。

**CGO_ENABLED=0**: 禁用 CGO。生成的二进制文件不依赖系统的 C 库（如 glibc），实现完全的纯 Go 静态编译，非常适合部署在 scratch 或 alpine 等轻量级 Docker 镜像中。

**GOOS=linux**: 指定目标操作系统为 Linux（实现跨平台交叉编译的关键参数）。

**GOARCH=amd64**: 指定目标 CPU 架构为 x86_64（64位）。

## 常用编译参数

**-o <file>**: 指定输出的可执行文件名称及路径（例如 go build -o bin/app main.go）。

**-ldflags "<flags>"**: 向链接器传递参数。常用 **-ldflags "-s -w"** 组合，其中 -s 去掉符号表和调试信息，-w 去掉 DWARF 调试信息，通常能让二进制文件体积减小 30% 以上。

**-trimpath**: 移除编译后的二进制文件中的本地绝对路径，确保不同机器编译出的文件哈希一致，提升构建的可复现性并保护开发路径隐私。

**-v**: 打印出正在编译的包名，方便观察依赖项和编译进度。

**-x**: 打印出编译过程中执行的具体底层命令（如调用 cmd/compile、link 等），常用于排查编译异常。

**-race**: 开启数据竞争检测，主要用于测试和开发阶段，能找出并发代码中的读写冲突问题。

## 检测脚本  

```bash title="check.sh"
#!/bin/bash

# 获取操作系统
GOOS=$(uname -s | tr '[:upper:]' '[:lower:]')

# 获取架构并映射为 Go 的命名规范
ARCH=$(uname -m)
case "$ARCH" in
    x86_64)
        GOARCH="amd64"
        ;;
    aarch64|arm64)
        GOARCH="arm64"
        ;;
    armv7l|armv8l)
        GOARCH="arm"
        ;;
    i386|i686)
        GOARCH="386"
        ;;
    riscv64)
        GOARCH="riscv64"
        ;;
    *)
        echo "不支持的架构: $ARCH"
        exit 1
        ;;
esac

echo "检测到平台: GOOS=$GOOS GOARCH=$GOARCH"
```
