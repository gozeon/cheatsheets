---
title: Mongo
category: DB
intro: See [Docs](https://www.mongodb.com/)
---

# 常用命令

### 版本

```bash
db.version()
```

### 索引

```bash
# 创建索引
db.foods.ensureIndex({name:1,  healthy:1})

# 查看索引
db.foods.getIndexes()

# 删除索引
db.foods.dropIndexes()
```

### 去重

删除重复数据(document)，以 name、healthy 重复为例，参考[链接](https://stackoverflow.com/questions/14184099/fastest-way-to-remove-duplicate-documents-in-mongodb)

```bash
# version 3.4.24
db.foods.aggregate([
    {
        $group: {
            _id: {
                name: "$name",
                health: "$healthy"
            },
            count: {
                $sum: 1
            },
            dups:{
                $addToSet: '$_id'
            }
        }
    },
    {
        $match: {
            count: {
                $gt: 1
            }
        }
    }
]).forEach(function(it) {
    // 剔除第一个
    it.dups.shift()

    // 删除其余的
    // db.foods.remove({_id: {$in: it.dups}});
    db.foods.deleteMany({_id: {$in: it.dups}})
})

```
