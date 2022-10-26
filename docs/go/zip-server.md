

上传zip文件，解压出静态目录

> zip 出现中文乱码使用 `unzip -O GBK xx.zip`

```go title="main.go"
package main

import (
	"archive/zip"
	"errors"
	"fmt"
	"io"
	"io/ioutil"
	"log"
	"os"
	"path/filepath"
	"regexp"
	"strings"
	"unicode/utf8"

	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/fiber/v2/middleware/logger"
	"golang.org/x/text/encoding/simplifiedchinese"
)

var index = `
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form method="post" action="/upload" enctype="multipart/form-data" accept-charset="utf-8">
        <input name="document" type="file" accept=".zip," required />
        <button type="submit">upload</button>
    </form>
    <fieldset>
        <legend>Index</legend>
        <ul>%s</ul>
    </fieldset>
</body>
</html>
`

func makeSureFolder(path string) {
	if _, err := os.Stat(path); errors.Is(err, os.ErrNotExist) {
		err := os.Mkdir(path, os.ModePerm)
		if err != nil {
			log.Fatal(err)
		}
	}
}

// https://golang.cafe/blog/golang-unzip-file-example.html
func unZip(dst, src string) (err error) {
	archive, err := zip.OpenReader(src)
	if err != nil {
		return err
	}
	defer archive.Close()

	for _, f := range archive.File {

		fmt.Println(utf8.Valid([]byte(f.Name)))
		fname := f.Name
		// 转GBK
		if utf8.Valid([]byte(fname)) != true {
			fname, _ = simplifiedchinese.GBK.NewDecoder().String(f.Name)
			//fname, _, _ := transform.String(simplifiedchinese.GBK.NewDecoder(), f.Name)
		}
		filePath := filepath.Join(dst, fname)
		fmt.Println("unzipping file ", filePath)

		if !strings.HasPrefix(filePath, filepath.Clean(dst)+string(os.PathSeparator)) {
			fmt.Println("invalid file path")
			return
		}
		if f.FileInfo().IsDir() {
			fmt.Println("creating directory...")
			os.MkdirAll(filePath, os.ModePerm)
			continue
		}

		if err := os.MkdirAll(filepath.Dir(filePath), os.ModePerm); err != nil {
			return err
		}

		dstFile, err := os.OpenFile(filePath, os.O_WRONLY|os.O_CREATE|os.O_TRUNC, f.Mode())
		if err != nil {
			return err
		}

		fileInArchive, err := f.Open()
		if err != nil {
			return err
		}

		if _, err := io.Copy(dstFile, fileInArchive); err != nil {
			return err
		}

		dstFile.Close()
		fileInArchive.Close()
	}
	return nil
}

func main() {
	makeSureFolder("public")
	app := fiber.New(fiber.Config{
		BodyLimit: 10 * 1024 * 1024,
	})
	app.Use(logger.New())
	app.Static("/", "./public")

	app.Get("/", func(c *fiber.Ctx) error {
		c.Set(fiber.HeaderContentType, fiber.MIMETextHTMLCharsetUTF8)

		var fileitem string
		files, err := ioutil.ReadDir("./public")
		if err != nil {
			log.Fatal(err)
		}
		for _, f := range files {
			fileitem += fmt.Sprintf("<li><a href='/%s/'>%s</a></li>", f.Name(), f.Name())
		}

		return c.SendString(fmt.Sprintf(index, fileitem))
	})

	// Routes
	app.Post("/upload", func(c *fiber.Ctx) error {
		// Get first file from form field "document":
		file, err := c.FormFile("document")
		if err != nil {
			return err
		}

		filename := fmt.Sprintf("./public/%s", file.Filename)
		ext := filepath.Ext(filename)
		matched, err := regexp.Match("^.zip$", []byte(ext))
		if err != nil {
			return err
		}
		if matched == false {
			return errors.New("only support .zip file.")
		}

		// Save file to root directory:
		err = c.SaveFile(file, filename)
		if err != nil {
			return err
		}
		err = unZip("./public", filename)
		if err != nil {
			return err
		}

		return c.Redirect("/")
	})

	// Start server
	log.Fatal(app.Listen(":8989"))
}


```
