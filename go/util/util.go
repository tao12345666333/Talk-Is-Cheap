package util

import "fmt"

func main() {
	s := []int{2, 3, 5, 7, 11, 13}
	fmt.Println("s ==", s)

	for i := 0; i < len(s); i++ {
		fmt.Printf("s[%d] == %d\n", i, s[i])
	}
}

func stringSliceIndex(s, subs []string) int {
	j := 0
	if len(subs) > 0 {
		for i, x := range s {
			if j < len(subs) && subs[j] == x {
				j++
			} else {
				j = 0
			}
			if len(subs) == j {
				return i + 1 - j
			}
		}
	}
	return -1
}

// StringSliceReplaceAt replaces the sub-slice old, with the sub-slice new, in the string
// slice s, returning a new slice and a boolean indicating if the replacement happened.
// requireIdx is the index at which old needs to be found at (or -1 to disregard that).
func StringSliceReplaceAt(s, old, new []string, requireIndex int) ([]string, bool) {
	idx := stringSliceIndex(s, old)
	if (requireIndex != -1 && requireIndex != idx) || idx == -1 {
		return s, false
	}
	out := append([]string{}, s[:idx]...)
	out = append(out, new...)
	out = append(out, s[idx+len(old):]...)
	return out, true
}
