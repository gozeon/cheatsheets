package main

import (
	"encoding/json"
	"fmt"
)

type Data struct {
	Value json.Number `json:"value"`
}

func main() {
	// JSON with int
	jsonInt := `{"value": 123}`
	var dataInt Data
	err := json.Unmarshal([]byte(jsonInt), &dataInt)
	if err != nil {
		fmt.Println("Error unmarshaling int:", err)
		return
	}
	intValue, err := dataInt.Value.Int64()
	if err != nil {
		fmt.Println("Error converting json.Number to int64 for int:", err)
		return
	}
	fmt.Printf("Parsed int value: %d (type: %T)\n", intValue, intValue)

	// JSON with string
	jsonString := `{"value": "456"}`
	var dataString Data
	err = json.Unmarshal([]byte(jsonString), &dataString)
	if err != nil {
		fmt.Println("Error unmarshaling string:", err)
		return
	}
	stringValue, err := dataString.Value.Int64() // json.Number handles string conversion
	if err != nil {
		fmt.Println("Error converting json.Number to int64 for string:", err)
		return
	}
	fmt.Printf("Parsed string value: %d (type: %T)\n", stringValue, stringValue)
}
