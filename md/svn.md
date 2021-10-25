---
title: SVN 常用命令 # 这是标题
category: svn,other, # 这是分类，用 ‘,’ 隔开
intro: '[官网](https://subversion.apache.org/)'
---

# 基础知识点

### 版本库结构

版本库一般的布局结构为 trunk(主干)、branches(分支)、tags(标签)

- `trunk` 就是开发的主线，一般项目都是导入到主线来开发的
- `branch` 一般是 trunk 某个版本的拷贝，如果你想在某一段时间单独对某个功能进行开发，而不像和其他功能混在一起，这时候 branches 是一个很好用的方式。
- `tags` 某个版本的记录。迭代开发时，在某个版本发布应用，为了做个记录，这时候打个 tag 很实用。发布后，线上出现了一个 bug，可以根据这个 tag 进行修复再发版本。

# 常用命令

### checkout

检出，将代码克隆到本地，类似 `git clone`

```bash
# 代码检出比较简单，执行以下命令，$project_name表示项目名称：
svn co svn://.../path $project_name
# 有时想检出某个历史版本，$version标识版本号：
svn co svn://.../path@$version $project_name
```

### commit

提交代码

```bash
# 所有文件
svn ci -m "更新说明"
# 只提交某个文件：
svn ci path_to_file -m "更新说明"
```

### update

更新代码，类似 `git pull/fetch`

```bash
svn update
```

# 分支

### 增加分支

增加一个分支，实际上就是把 trunk 复制到 branches 目录下，起一个特定的名字，常用版本号

```bash
svn copy svn://../trunk/project svn://../branches/project_buy -m "添加购买功能分支"
```

### 合并分支

增加一个分支，实际上就是把 trunk 复制到 branches 目录下，起一个特定的名字，常用版本号

```bash
# setp 1
# r1:r2表示从版本记录r1和r2之间的变化合并到当前工作目录中。
svn merge -r r1:r2 svn://../branches/project_buy ./

# setp 2
# 提交
svn ci -m "合并购买功能到主干"

# setp 3 （可选）
# 删除分支
svn delete svn://../branches/project_buy -m "删除购买功能到主干"
```

# 标签

### 创建

```bash
svn copy svn://../trunk/project svn://../tags/project_tag1 -m "创建标签1"
```

### 删除

```bash
svn rm svn://../tags/project_tag1 -m "删除标签1"
```

# 版本

### 版本回退

```bash
# 没有提交的代码回退
svn revert svn://../path_to_file

# 已提交代码回退
svn merge -r r2:r1 svn://../path_to_file merge_file
```

# 其他

### 常用命令

```bash
# 查看版本历史记录, 按n进行下翻，按q退出
svn log | more

# 查看版本历史记录，并看修改了哪些文件
svn log -v | more

# 查看文件变化diff, 本地文件和版本库的变化
svn diff path_to_file | more

# 版本库版本的变化
svn diff -c r svn://../path_to_file | more
```
