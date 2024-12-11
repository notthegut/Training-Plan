// Map relate something to a key, for example have a map of strings to strings with the value bar related to the key foo
package main

import "fmt"

func main() {
	var m map[string]int                   //declare a map
	fmt.Println(m)                         //map[] nil
	m = map[string]int{"foo": 1, "bar": 2} //map literal
	fmt.Println(m)                         // map[foo:1 bar:2]

	fmt.Println(m["foo"]) //lookup value in map
	m["bar"] = 99         //update value in map

	delete(m, "foo") //Remove an entry from map
	m["baz"] = 418   //Add value to a map

	fmt.Println(m)        //map[bar:99, baz:418]
	fmt.Println(m["foo"]) //Returns the value 0 as it does not exists in the map, will always return a value if something isn no in the map
	v, ok := m["Foo"]     //comma okay syntax verifies presents
	fmt.Println(v, ok)    // 0 , false to show not in map

	m2 := map[string]int{
		"foo": 1,
		"bar": 2,
		"baz": 3,
	}

	m3 := m2 //maps are like slices, copied by reference, use map.clone to clone

	m2["foo"], m3["bar"] = 99, 42 //update values in maps
	fmt.Println(m2)
	fmt.Println(m3) //For both will be map[foo:99 bar:42 baz:3], the data is shared

	//Like before maps are not comparible
}
