package main

import (
	"fmt"
)

type V struct {
	X int
	Y string
}

var pow = []int{1, 2, 4, 8}

type Vertex struct {
	string
}

var m map[string]Vertex

func main() {
	var p *int
	i := 42
	p = &i
	fmt.Println(i)
	fmt.Println(p)
	fmt.Println(*p)

	s := V{1, "2"}
	sp := &s

	fmt.Println(s.Y)
	fmt.Println(sp)

	a := make([]int, 5)

	fmt.Println(cap(a))
	fmt.Println(len(a))
	fmt.Println(a)

	printSlice("a", a)

	for i, v := range pow {
		fmt.Printf("%d is %d\n", i, v)
	}

	var ss []int
	printSlice("ss", ss)
	ss = append(ss, 6)
	printSlice("ss", ss)
	ss = append(ss, 6)
	printSlice("ss", ss)
	ss = append(ss, 6)
	printSlice("ss", ss)

	for i, v := range ss {
		fmt.Printf("%d is %d; ", i, v)
	}

	m = make(map[string]Vertex)
	m["Tao"] = Vertex{
		"Beier",
	}
	fmt.Println("")
	fmt.Println(m["Tao"])

	var nm = map[string]Vertex{
		"t1": Vertex{
			"t1v",
		},
		"t2": Vertex{
			"t2v",
		},
	}
	fmt.Println(nm)

}

func printSlice(s string, x []int) {
	fmt.Printf("%s len=%d cap=%d %v\n",
		s, len(x), cap(x), x)
}
