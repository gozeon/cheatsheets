package main

import (
	"encoding/json"
	"fmt"

	"github.com/samber/lo"
)

type Item struct {
	Id       int
	Name     string
	Pid      int
	Children []Item
}

func toNested(list []Item, pid int) []Item {
	return lo.Reduce(list, func(agg []Item, item Item, index int) []Item {
		if pid == item.Pid {
			item.Children = toNested(list, item.Id)
			return append(agg, item)
		} else {
			return agg
		}

	}, []Item{})
}

func main() {

	list := []Item{
		Item{
			Id:   1,
			Name: "1",
			Pid:  0,
		},
		Item{
			Id:   2,
			Name: "1-2",
			Pid:  1,
		},
		Item{
			Id:   3,
			Name: "3",
			Pid:  0,
		},
		Item{
			Id:   4,
			Name: "4",
			Pid:  0,
		},
		Item{
			Id:   5,
			Name: "4-5",
			Pid:  4,
		},
		Item{
			Id:   6,
			Name: "1-2-6",
			Pid:  2,
		},
	}

	result := toNested(list, 0)
	fmt.Printf("%v\n", result)

	jsonb, _ := json.Marshal(result)
	fmt.Println(string(jsonb))
}

