package main

import (
	"fmt"
	"slices"
)

//A slice is a subset of an underlying array. So a slice is a certain part of an array

//Slices do not contain their own data but they are instead a data reference point. Any changes in the original array make changes to the slice
//However when we make a change to the slice, it also makes that same change in the slice.

//Slice is a dynamic data type that can grow over time

// var s []int slices of ints
func main() {
	var s []int                //slices of ints
	s = []int{1, 2, 3}         //slice literal
	fmt.Println(s[1])          //2
	s[1] = 99                  //update value
	fmt.Println(s)             //[1 99 3]
	s = append(s, 5, 10, 15)   // Add element to the slice
	fmt.Println(s)             //[1 99 3 5 10 15]
	s = slices.Delete(s, 1, 3) //Removed indicies 1 and 3 from the slice

	s2 := []string{"foo", "bar", "baz"}
	s3 := s2                     //Slices are coppied by reference, if yu want a copie by value use slices.Clone
	s2[0], s3[2] = "qux", "fred" //update value in slices
	fmt.Println(s2, s3)          // We will see ["qux, "bar", "fred"] for both, as they are naturally copied by reference not data
}
