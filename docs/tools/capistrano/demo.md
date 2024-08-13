### capistrano

部署工具，需要选择scm进行代码管理，默认使用git，如果本地编译上传需要自定义scm，使用ansible的学习成本较高，且对部分系统支持不好，如alpine。

### 初始化项目

```bash
cap install
cap install STAGES=local,dev,test,prod
```

### 运行

```bash
cap <stage> deploy
```

### 可参考项目

https://github.com/gozeon/code-collections/tree/master/ruby/cap
