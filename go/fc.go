package main

import (
	"fmt"
	"math"
	"runtime"
	"time"
)

func loop() {
	sum := 0

	for i := 0; i < 100; i += 5 {
		sum += i
		if sum < 50 {
			fmt.Println(i)
		} else {
			fmt.Println(sum)
		}
	}

	fmt.Println(sum)
}

func Sqrt(x float64) float64 {
	z := 1.0
	for true {
		tmp := z - (z*z-x)/(2*z)
		fmt.Println(tmp)
		if tmp == z || math.Abs(tmp-z) < 0.0000000001 {
			break
		}
		z = tmp
	}
	return z
}

func r() {
	fmt.Print("go runs on ")
	switch os := runtime.GOOS; os {
	case "darwin":
		fmt.Println("mac os")
	default:
		fmt.Printf("%s.\n", os)
	}
}

func main() {
	//loop()
	//fmt.Println(Sqrt(3))
	//fmt.Println(math.Sqrt(3))
	defer r()
	fmt.Println(time.Now())
}
