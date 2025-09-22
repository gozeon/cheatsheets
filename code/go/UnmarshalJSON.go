package main

import (
	"encoding/json"
	"fmt"
	"strconv"
)

type FlexibleInt int

func (fi *FlexibleInt) UnmarshalJSON(b []byte) error {
	// Try to unmarshal as an int
	var i int
	if err := json.Unmarshal(b, &i); err == nil {
		*fi = FlexibleInt(i)
		return nil
	}

	// If that fails, try to unmarshal as a string and convert
	var s string
	if err := json.Unmarshal(b, &s); err == nil {
		parsedInt, err := strconv.Atoi(s)
		if err != nil {
			return fmt.Errorf("failed to convert string to int: %w", err)
		}
		*fi = FlexibleInt(parsedInt)
		return nil
	}

	return fmt.Errorf("failed to unmarshal as int or string: %s", string(b))
}

type AnotherData struct {
	Value FlexibleInt `json:"value"`
}

func main() {
	// JSON with int
	jsonInt := `{"value": 789}`
	var dataInt AnotherData
	err := json.Unmarshal([]byte(jsonInt), &dataInt)
	if err != nil {
		fmt.Println("Error unmarshaling int:", err)
		return
	}
	fmt.Printf("Parsed int value: %d (type: %T)\n", dataInt.Value, dataInt.Value)

	// JSON with string
	jsonString := `{"value": "1011"}`
	var dataString AnotherData
	err = json.Unmarshal([]byte(jsonString), &dataString)
	if err != nil {
		fmt.Println("Error unmarshaling string:", err)
		return
	}
	fmt.Printf("Parsed string value: %d (type: %T)\n", dataString.Value, dataString.Value)
}
