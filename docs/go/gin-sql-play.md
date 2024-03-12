## 在线执行sql

```go title="example.go"
package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"html/template"
	"local-gin/utils"

	"github.com/gin-contrib/cors"
	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()
	corsConfig := cors.DefaultConfig()
	corsConfig.AllowAllOrigins = true
	corsConfig.AllowHeaders = []string{"*"}
	r.Use(cors.New(corsConfig))
	r.GET("/ping", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "pong",
		})
	})

	dbs := []string{"a", "b", "c", "d"}
	htmlString := `
	<head>
		<link href="https://cdn.bootcdn.net/ajax/libs/monaco-editor/0.20.0/min/vs/editor/editor.main.min.css" rel="stylesheet">
	</head>
	<body style="margin: 0;">
		<div
			style="height: 100vh;width: 100vw;display: grid; grid-template-columns: repeat(2, 1fr);grid-template-rows: 40px 1fr;">
			<div style="display: flex;align-items: center; padding: 10px;">
				<form method="post" id="play" style="margin:0;">
					<label for="">
						DB:{{.DbValue}}
						<select name="db" id="db">
						{{range .Dbs}}
						<option value="{{ . }}" {{if eq . $.DbValue }}selected{{end}}>{{ . }}</option>
						{{end}}
							
						</select>
					</label>
					<input type="hidden" name="sql" id="sql" value="{{.Sql}}" />
				</form>
			</div>
			<div style="display: flex; align-items: center;">
				<input type="submit" form="play" value="Run" />
			</div>
			<div id="editor"></div>
			<div id="view"></div>
		</div>
		<script src="https:///www.unpkg.com/monaco-editor@0.47.0/min/vs/loader.js"></script>
		<script>
		require.config({ paths: { 'vs': 'https:///www.unpkg.com/monaco-editor@0.47.0/min/vs' } });
		require(['vs/editor/editor.main'], function () {
			sqlEditor = monaco.editor.create(document.getElementById('editor'), {
                value: '{{.Sql}}',
    			      language: 'sql',
            });
			
			sqlEditor.onDidBlurEditorText(function(){
				document.querySelector('#sql').value = sqlEditor.getValue()
			})
			
			viewEditor = monaco.editor.create(document.getElementById('view'), {
                value: '{{.Result}}',
    			      language: 'json',
                readOnly: true
            });
		})
		</script>
	</body>
	`
	type sqlData struct {
		Dbs     []string
		DbValue string `form:"db"`
		Sql     string `form:"sql"`
		Result  string
	}
	t, _ := template.New("edior").Parse(htmlString)
	run := r.Group("play")
	{
		run.GET("", func(ctx *gin.Context) {
			writer := bytes.NewBufferString("")
			t.Execute(writer, sqlData{
				Dbs: dbs,
			})
			ctx.Header("content-type", "text/html; charset=utf-8")
			ctx.String(200, writer.String())
		})

		run.POST("", func(ctx *gin.Context) {
			var params sqlData
			if err := ctx.ShouldBind(&params); err != nil {
				fmt.Println(params)
				params.Result = err.Error()
			}
			if len(params.DbValue) == 0 || len(params.Sql) == 0 {
				params.Result = "参数错误"
			} else {
				db, err := utils.GetDBConnection(params.DbValue)
				if err != nil {
					params.Result = err.Error()
				} else {
					var result []map[string]interface{}
					r := db.Raw(params.Sql).Find(&result)
					if r.Error != nil {
						params.Result = r.Error.Error()
					} else {
						b, _ := json.MarshalIndent(result, "", "  ")
						params.Result = string(b)
					}
				}
			}

			writer := bytes.NewBufferString("")
			params.Dbs = dbs
			t.Execute(writer, params)
			ctx.Header("content-type", "text/html; charset=utf-8")
			ctx.String(200, writer.String())
		})
	}

	r.Run(":8200")
}

```
