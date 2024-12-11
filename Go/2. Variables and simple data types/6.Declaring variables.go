package main

import "fmt"

//How do we create a variable and assign a simple data type to them

//Use var

var myName string

//We first use var to declare the variable
//Then we give the name if the variable
//And then we give the data type of the variable
//If we do not give the value of the variable then it will default to 0 for its value

//If you want it to be given a value then we can use a initialiser of =

var theName string = "Zain"

//However, go is clever, it cna infer the type from the intialiser, meaning we can drop the type of data type

var daName = "Zain"

//However the most common one you will see is the short declartion syntax,

func main() {
	deName := "Zain"
	fmt.Println(deName)
}

//Can use documentation at https://pkg.go.dev/builtin
