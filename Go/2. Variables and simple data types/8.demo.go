package main

import (
	"fmt"
	"strings"
)

func main() {
	//var name string = "Dent, Arthur"
	//var score = 87
	//score := 87

	name, score := "Dent, Arthur", 87

	fmt.Println("Student scores")
	fmt.Println(strings.Repeat("-", 14)) //Part of the standard library, which we can find at https://pkg.go.dev/std
	fmt.Println(name, score)
}
