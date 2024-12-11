package main

import (
	"fmt"
	"strings"
)

func main() {
	//var name string = "Dent, Arthur"
	//var score = 87
	//score := 87
	//name, score := "Dent, Arthur", 87

	type score struct {
		name  string
		score int
	}
	scores := []score{
		{name: "Dent, Arthur", score: 87},
		{name: "MacMillan, Tricia", score: 97},
		{name: "Prefect, Ford", score: 96},
	}

	fmt.Println("Student scores")
	fmt.Println(strings.Repeat("-", 14)) //Part of the standard library, which we can find at https://pkg.go.dev/std
	fmt.Println(scores[0].name, scores[0].score)
	fmt.Println(scores[1].name, scores[1].score)
	fmt.Println(scores[2].name, scores[2].score)
}
