package main

import "fmt"

func main() {
	var li = []string{"a", "b", "c"}

	s("SET", "a", "b")

	s("SET", []interface{}{"a", "b"})
	s("SET", []interface{}{"a", "b"}...)

	s("SET", []interface{}{li})
	s("SET", []interface{}{li[1:]})
	s("SET", []interface{}{li[1:]}...)

	var n []interface{}
	var d = append(n, li)
	s("SET", d)
	s("SET", d...)

	var m = make([]interface{}, len(li[1:]))
	for i, v := range li[1:] {
		m[i] = v
	}
	s("SET", m)
	s("SET", m...)
}

func s(cmd string, t ...interface{}) {
	fmt.Println(len(t))
	fmt.Printf("%q \n", cmd)
	fmt.Printf("%q \n", t)

}
