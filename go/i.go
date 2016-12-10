package main

import (
	"fmt"
	"os"
)

type Reader interface {
	Read(b []byte) (n int, err error)
}

type Writer interface {
	Write(b []byte) (n int, err error)
}

type ReadWriter interface {
	Reader
	Writer
}

type Person struct {
	Name string
	Age  string
}

func (p Person) String() string {
	return fmt.Sprintf("%v (%v years)", p.Name, p.Age)
}

func (p *Person) T() {
	p.Name = "T"
	p.Age = "Tage"

	fmt.Println(p)
}

func (p Person) Nt() {
	p.Name = "T"
	p.Age = "Tage"

	fmt.Println(p)
}

func main() {
	var w Writer
	w = os.Stdout

	fmt.Fprintf(w, "heww \n")

	a := Person{"Anz", "66"}
	fmt.Println(a)

	a.Nt()
	fmt.Println(a)

	a.T()
	fmt.Println(a)

	s := func(a, b int) int { return a + b }(6, 9)
	fmt.Println(s)
}
