// Like an array but it is a collection of different data types
package main

import "fmt"

//Only limitation is have to define fields at the time of writing a structs

func main() {
	var s struct {
		name string
		id   int
	}

	fmt.Println(s) //Structs are value types

	s.name = "Arthur"   //Assign value to field
	fmt.Println(s.name) //query value of field

	type myStruct struct {
		name string
		id   int
	} //Creat ea custm type based on struct

	var d myStruct //Declare variable with custom type

	d = myStruct{
		name: "Arthur",
		id:   42,
	}
	fmt.Println(d)

	d2 := d
	d.name = "Tricia"  //Stricts are copied by value
	fmt.Println(d, d2) //{Tricia}, {Arthur}
}
