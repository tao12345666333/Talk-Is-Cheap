package main

import (
	"fmt"
	"sync"
	"time"
)

func say(s string) {
	for i := 0; i < 5; i++ {
		time.Sleep(100 * time.Millisecond)
		fmt.Println(s)
	}
}

func sum(a []int, c chan int) {
	sum := 0
	for _, v := range a {
		sum += v
	}
	c <- sum
}

func fibnocci(c, quit chan int) {
	x, y := 0, 1
	for {
		select {
		case c <- x:
			x, y = y, x+y
		case <-quit:
			fmt.Println("quit")
			return
		}
	}
}

type SafeCounter struct {
	v   map[string]int
	mux sync.Mutex
}

func (c *SafeCounter) Inc(key string) {
	c.mux.Lock()
	c.v[key]++
	c.mux.Unlock()
}

func (c *SafeCounter) Value(key string) int {
	c.mux.Lock()
	defer c.mux.Unlock()
	return c.v[key]
}

func main() {
	go say("w")
	say("hi~")

	a := []int{6, 8, 4, 2, 1, 0}

	c := make(chan int)

	go sum(a[:len(a)/2], c)
	go sum(a[len(a)/2:], c)
	go sum(a[len(a)/2:], c)
	x, y := <-c, <-c

	fmt.Println(x, y, x+y)

	c2 := make(chan int)
	quit := make(chan int)
	go func() {
		for i := 0; i < 10; i++ {
			fmt.Println(quit)
			fmt.Println(<-c2)
		}
		quit <- 0
	}()

	fibnocci(c2, quit)

	tick := time.Tick(100 * time.Millisecond)
	boom := time.After(500 * time.Millisecond)

	for {
		select {
		case <-tick:
			fmt.Println("tick.")
		case <-boom:
			fmt.Println("BOOM!")
			return
		default:
			fmt.Println("        . ")
			time.Sleep(50 * time.Millisecond)
		}
	}

	cc := SafeCounter{v: make(map[string]int)}
	for i := 0; i < 1000; i++ {
		go cc.Inc("somekey")
	}

	time.Sleep(time.Second)
	fmt.Println(cc.Value("somekey"))
}
