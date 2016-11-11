package main

import (
	"fmt"
)

type V struct {
	X int
	Y string
}

var pow = []int{1, 2, 4, 8}

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

}

func printSlice(s string, x []int) {
	fmt.Printf("%s len=%d cap=%d %v\n",
		s, len(x), cap(x), x)
}
