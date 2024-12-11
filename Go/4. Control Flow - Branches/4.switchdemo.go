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

	fmt.Println("Select score to print(1-3):")
	var option string
	fmt.Scanln(&option) //Go will take the input and store that value as the value of option, can use that to make a decision, & sign used to make the data be copied to the address of the variable

	fmt.Println("Student scores")
	fmt.Println(strings.Repeat("-", 14)) //Part of the standard library, which we can find at https://pkg.go.dev/std
	//not very efficient to use if statements for this scenario, so lets use swithc
	var index int
	// if option == "1" { //should use strconv package in production
	// 	index = 0
	// } else if option == "2" {
	// 	index = 1
	// } else if option == "3" {
	// 	index = 2
	// } else {
	// 	fmt.Println("Unknown option, defaulting to 1")
	// 	index = 1
	// }
	switch option {
	case "1":
		index = 0
	case "2":
		index = 1
	case "3":
		index = 2
	default:
		fmt.Println("Unknown option, defaulting to 1")
		index = 1
	}

	fmt.Println(scores[index].name, scores[index].score)

}
