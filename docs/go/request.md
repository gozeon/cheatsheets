## http封装

```go title="helper/http.go"

package helper

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"net/url"
	"strings"
)

type HTTPMethod int

const (
	GET HTTPMethod = iota
	POST
	PUT
	PATCH
	DELETE
)

func (s HTTPMethod) String() string {
	switch s {
	case GET:
		return "GET"
	case POST:
		return "POST"
	case PUT:
		return "PUT"
	case PATCH:
		return "PATCH"
	case DELETE:
		return "DELETE"
	}
	return "unknown"
}

func MakeHTTPRequest[T any](urlFull string, method string, headers map[string]string, query url.Values, body io.Reader, responseType T) (T, error) {
	client := http.Client{}

	// format url
	u, err := url.Parse(urlFull)
	if err != nil {
		return responseType, err
	}

	// format query
	q := u.Query()

	for k, v := range query {
		q.Set(k, strings.Join(v, ","))
	}
	u.RawQuery = q.Encode()

	// init http
	req, err := http.NewRequest(method, u.String(), body)
	if err != nil {
		return responseType, err
	}
	// init header
	for k, v := range headers {
		req.Header.Set(k, v)
	}
	// do request
	res, err := client.Do(req)
	if err != nil {
		return responseType, err
	}
	// warning empty response
	if res == nil {
		return responseType, fmt.Errorf("")
	}
	defer res.Body.Close()

	// no 200
	if res.StatusCode != http.StatusOK {
		return responseType, fmt.Errorf("")
	}
	// read body
	resP, err := io.ReadAll(res.Body)
	if err != nil {
		return responseType, err
	}

	var resO T
	err = json.Unmarshal(resP, &resO)
	if err != nil {
		return responseType, err
	}

	return resO, nil
}


```

使用

```go
	testurl := "http://localhost:8082"
	
	headers := map[string]string{
		"Accept": "application/vnd.github.v3+json",
	}

	queryParameters := url.Values{}
	queryParameters.Add("time", time.Now().GoString())

	var response Info
	
	// get
	response, err := helper.MakeHTTPRequest(testurl+"/get", helper.GET.String(), headers, queryParameters, nil, response)
	if err != nil {
		panic(err)
	}
	fmt.Println(response)

	// post any response
	var res map[string]interface{}
	body := bytes.NewBufferString(`{"name": "test"}`)
	res, err = helper.MakeHTTPRequest(testurl+"/post", helper.POST.String(), headers, nil, body, res)
	if err != nil {
		panic(err)
	}
	fmt.Println(res)

```


