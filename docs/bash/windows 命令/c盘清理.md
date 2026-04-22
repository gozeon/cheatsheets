
## 下载  WizTree

查看具体文件

## hiberfil.sys 文件

如果你平时习惯关机或睡眠（Sleep），而不是“休眠”（Hibernate），可以安全地执行此操作：

```cmd
# 彻底删除 hiberfil.sys
powercfg -h off

# 如果你确实需要休眠功能，但觉得它太占空间，可以将其设置为“压缩模式”
powercfg /h /type reduced
```

## docker 文件迁移

> 使用软链方式，按照这个方式其实可以把Download、Temp、APPData都连接到D盘

1. 退出docker程序
2. 关闭wsl `wsl --shutdown`
3. C盘docker做好备份，先复制一份到D盘
4. 制作软链 `mklink /j "C:\Users\admin\AppData\Local\Docker" "D:\docker\Docker"`
5. 启动docker并验证
6. 将C盘docker移动到D盘

## 移动命令可以参考

robocopy "C:\源" "D:\目标" /E /MOVE /MT:32 /XJ
/E (Everything)：递归拷贝所有子文件夹，包括空的。
/MOVE：搬完就删掉 C 盘的源文件。注意： 它是在确认 D 盘写入成功后才删，比“剪切”安全得多。
/MT:32：开启 32 路并行，压榨磁盘带宽。
/XJ (eXclude Junctions)：极其重要。它会跳过目录联接点。如果不加这个，遇到软链接时 Robocopy 可能会陷入循环（无限递归），导致磁盘写满。
/MIR (Mirror)：镜像模式。如果源端删了文件，目标端也会跟着删。常用于备份。
