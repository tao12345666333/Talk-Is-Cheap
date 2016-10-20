package main

import "fmt"

func swap(x, y string) (string, string) {
	return y, x
}

func main() {
	a, b := swap("f", "b")
	fmt.Println(a, b)
}
