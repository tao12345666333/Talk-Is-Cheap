package main

import (
	"fmt"
)

type V struct {
	X int
	Y string
}

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

}

func printSlice(s string, x []int) {
	fmt.Printf("%s len=%d cap=%d %v\n",
		s, len(x), cap(x), x)
}
