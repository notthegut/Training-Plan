package main

const a = 42 //Const a will alwyas have the value 42. It is implicitly typed so anywhere we write the letter a it will be replaced with the number 42
//42 not given a type so it can be intepreted as different data types depending on what the compiler needs it to be depending on the situation

const b string = "hello, world" //This EXPlICITLY typed constant restricts the usage of the constant to be only one type of data types

const c = a //one constant can be assigned to another

const (
	d = true
	e = 3.14
)

//Can denote multiple constants at once using this way

const f = 2 * 5 //Constant expression, done at compiler time.Cannot use a function that cannot be complied in compile time

const g = "hello," + "world" //Can concatonate strings together ina constant
