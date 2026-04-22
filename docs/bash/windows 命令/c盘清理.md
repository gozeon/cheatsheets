
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
