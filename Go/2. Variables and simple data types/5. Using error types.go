package main

//Error types are built-in interface trype for representing a eror condition, with a nil value representing no error
//Seen as first class citizens, to the point they are bulit-in to the language

type error interface {
	Error() string
}

//This is what they look like
