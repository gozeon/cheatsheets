package main

import (
    "encoding/json"
    "log"
    "net/http"
    "strings"

    "github.com/gin-gonic/gin"
    "gorm.io/driver/mysql"
    "gorm.io/gorm"
)

// DB 变量
var db *gorm.DB

// 初始化数据库连接
func initDB() {
    var err error
    dsn := "user:password@tcp(127.0.0.1:3306)/dbname?charset=utf8mb4&parseTime=True&loc=Local"
    db, err = gorm.Open(mysql.Open(dsn), &gorm.Config{})
    if err != nil {
        log.Fatal("failed to connect to database:", err)
    }
}

// 执行 SQL 语句
func executeSQL(c *gin.Context) {
    var request struct {
        SQL string `json:"sql"`
    }
    
    if err := c.ShouldBindJSON(&request); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": "Invalid request"})
        return
    }

    sql := strings.TrimSpace(request.SQL)
    var result interface{}

    // 判断 SQL 类型并执行相应操作
    switch {
    case strings.HasPrefix(sql, "SELECT"):
        rows, err := db.Raw(sql).Rows()
        if err != nil {
            c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
            return
        }
        defer rows.Close()

        columns, err := rows.Columns()
        if err != nil {
            c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
            return
        }

        results := []map[string]interface{}{}
        for rows.Next() {
            values := make([]interface{}, len(columns))
            for i := range values {
                values[i] = new(interface{})
            }
            if err := rows.Scan(values...); err != nil {
                c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
                return
            }

            row := make(map[string]interface{})
            for i, col := range columns {
                val := *(values[i].(*interface{}))
                switch v := val.(type) {
                case []byte:
                    row[col] = string(v)
                default:
                    row[col] = v
                }
            }
            results = append(results, row)
        }
        result = results

    case strings.HasPrefix(sql, "INSERT"), strings.HasPrefix(sql, "UPDATE"), strings.HasPrefix(sql, "DELETE"):
        if err := db.Exec(sql).Error; err != nil {
            c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
            return
        }
        result = gin.H{"message": "Query executed successfully"}

    default:
        c.JSON(http.StatusBadRequest, gin.H{"error": "Unsupported SQL statement"})
        return
    }

    c.JSON(http.StatusOK, result)
}

func main() {
    // 初始化数据库
    initDB()

    // 创建 Gin 路由
    r := gin.Default()

    // 设置执行 SQL 的路由
    r.POST("/execute", executeSQL)

    // 启动服务器
    if err := r.Run(":8080"); err != nil {
        log.Fatal("failed to start server:", err)
    }
}
