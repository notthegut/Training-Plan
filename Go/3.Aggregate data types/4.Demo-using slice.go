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
	students := []string{"Dent, Arthur",
		" MacMilllan, Tricia",
		"Prefect, Ford",
	}
	scores := []int{87, 96, 64}

	fmt.Println("Student scores")
	fmt.Println(strings.Repeat("-", 14)) //Part of the standard library, which we can find at https://pkg.go.dev/std
	fmt.Println(students[0], scores[0])
	fmt.Println(students[1], scores[1])
	fmt.Println(students[2], scores[2])
}
