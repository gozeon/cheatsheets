

查找含有`console.log`的文件具体行，并打印git 提交用户，字符串截取参考[链接](http://c.biancheng.net/view/1120.html)

```bash title="test.bash"
#!/bin/bash

searhstr="console.log"
bashfile="test.bash"

for line in `grep -rn $searhstr . --exclude=$bashfile`

do

    # echo "line: $line"

    # 获取file
    file=${line%%:*}
    # echo "file: $file"

    # 获取行号
    linenum=${line%:*}
    linenum=${linenum#*:}
    # echo "linenum: $linenum"


    # 获取git提交用户
    author=`git blame -p -L $linenum $file | grep "^author "`
    author=${author#* }
    # echo $author


    echo "$file $linenum $author"
done

```
