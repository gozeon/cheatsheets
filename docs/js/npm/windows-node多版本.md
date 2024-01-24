## 下载可执行文件版本
Windows Binary (.zip)，解压到一个目录

## 新建cmd文件

> 使用的时候，将`npm.cmd`文件拷过去就行，运行命令如`npm.cmd start`

```cmd title="npm.cmd"
:: Created by npm, please don't edit manually.
@ECHO OFF

SETLOCAL

SET "NODE_EXE=<改成自己的>\node.exe"
set PATH=<改成自己的>;%PATH%



SET "NPM_CLI_JS=<改成自己的>\node_modules\npm\bin\npm-cli.js"

"%NODE_EXE%" "%NPM_CLI_JS%" %*

```
