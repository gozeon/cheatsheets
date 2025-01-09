# 查看binlog是否开启

```sql
show variables like '%log_bin%';
```

# 查看最新binlog文件名称

```sql
show master status ;
```

# 查看binlog日志, 建议加limit, 表示最新20条

```sql
show binlog events in 'mysql-bin.008187'  limit 20;
```

# 生成新的log文件, 如果当前是mysql-bin.000001, 那就进入mysql-bin.000002

```sql
FLUSH LOGS;
```

# 查看二进制日志文件内容

```bash
mysqlbinlog /path/to/mysql-bin.000001

# 会展示sql语句
mysqlbinlog -v /path/to/mysql-bin.000001
mysqlbinlog -vv /path/to/mysql-bin.000001
```

# 根据位置查看

```bash
mysqlbinlog --start-position=100 --stop-position=200 /path/to/mysql-bin.000001
```

# 根据时间查看

```bash
mysqlbinlog --start-datetime="2025-01-01 00:00:00" --stop-datetime="2025-01-02 00:00:00" /path/to/mysql-bin.000001
```

# 回滚至误操作前，上述同理

```bash
mysqlbinlog --stop-datetime="2025-01-09 10:00:00" /path/to/mysql-bin.000001 | mysql -u root -p your_database
```

# 参考

- https://dev.mysql.com/doc/refman/8.4/en/binary-log.html
- https://dev.mysql.com/doc/refman/8.4/en/mysqlbinlog.html
- https://dev.mysql.com/doc/refman/8.4/en/mysqlbinlog-row-events.html
- https://help.aliyun.com/zh/rds/apsaradb-rds-for-mysql/apsaradb-rds-for-mysql-remotely-obtains-and-parses-binlog-logs
- https://help.aliyun.com/zh/rds/apsaradb-rds-for-mysql/restoration-1/
- https://cloud.tencent.com/developer/article/1922672
- https://www.cnblogs.com/hld123/p/17115848.html


# 思路

- 把数据还原上一个状态，如一条数据被删除，不仅要找到insert时候的日志，还要找到后续的update。
- 如果事务复杂，记得锁库锁表
  
# 简单例子

表`users`插入一条数据，模拟误删，恢复这条数据

## 准备数据

> 如果不影响其他，可手动切一个新的日志文件


```sql

-- 创建数据库
CREATE DATABASE IF NOT EXISTS test_db;

-- 使用 test_db 数据库
USE test_db;

-- 创建 users 表
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

-- 插入初始数据
INSERT INTO users (name, email) VALUES
('Alice', 'alice@example.com'),
('Bob', 'bob@example.com'),
('Charlie', 'charlie@example.com');

```

查看当前数据

```sql
select * from users;
```
### 模拟误删除

```sql
insert into users (name, email) values('abc', 'abc');
delete from users where id=4;
```

### 查看binlog的event

```sql
show master status;
show binlog events in 'mysql-bin.008187'  limit 20;
```

### 恢复被误删除的数据

```bash
mysqlbinlog --start-position=12 --stop-position=13 /var/lib/mysql/binlog.000001 | mysql
```

查看结果

```sql
select * from users;
```


