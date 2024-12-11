package main

import "fmt"

//Like youve seen before 0 is the first index in an array
//They are static data structures

var arr [3]int //array of 3 ints

func main() {
	fmt.Println(arr)
	arr = [3]int{1, 2, 3} //Defines all the indexes in the array
	fmt.Println(arr)
	arr[1] = 99 //Updates an individual index in the array
	fmt.Println(arr)
	fmt.Println(len(arr)) //Gives the length of the array
	arr2 := arr           //arrays are copies by value, every element is going to be copied in arr2
	fmt.Println(arr2)
	arr[2] = 27
	fmt.Println(arr)
	fmt.Println(arr2) //Even tho we have changed the value of arr after declaring them the same, it doenst change for arr2 as it is copying its value, not its location, they are independent and store their own memory
}
