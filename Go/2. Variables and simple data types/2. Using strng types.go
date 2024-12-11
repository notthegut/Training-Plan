package main

import "fmt"

//There are 2 types of strings in golang

//"This is a string" - this is an interpreted string
//`This is also a string`- this is a raw string

//The difference between them is one uses double ticks the other uses back ticks
//Technically a intepreted string is and form of escape sequence used in the string

//Heres how it works

func main() {
	fmt.Println("This is an escape character: \n it creates a newline")

	main2()
}

//if you run this you well see that a new line is made for the second half of the code after the \n. Thats the key difference
//You would not be able to do this in the raw string, it will print exactly what is written, without making a new line

//However you can make a new line encoded into the string, and it will od the same thing as follows:

func main2() {
	fmt.Println(`This is an escape character
	it creates a newline`)
}
