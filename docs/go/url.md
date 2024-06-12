
## url 增加query

https://github.com/google/go-querystring  


```go title="uri.go"
func UrlAppend(uri string, obj map[string]string) string {
	u1, err := url.Parse(uri)
	if err != nil {
		return uri
	}
	q := u1.Query()
	for k, v := range obj {
		q.Add(k, v)
	}
	u1.RawQuery = q.Encode()
	return u1.String()
}
```
