package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func sameLetter(a, b byte) bool {
	return a^32 == b
}

func react(polymer string) string {
	i := 0
	for {
		if i >= len(polymer)-1 {
			break
		} else if sameLetter(polymer[i], polymer[i+1]) {
			polymer = polymer[:i] + polymer[i+2:]
			i = max(i-1, 0)
		} else {
			i++
		}
	}
	return polymer
}

func main() {
	b, err := ioutil.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}

	polymer := string(b)
	fmt.Println("p1", len(react(polymer)))

	smallest := 999999
	for c := 'a'; c <= 'z'; c++ {
		transform := func(r rune) rune {
			if r == c || r == c-32 {
				return -1
			}
			return r
		}
		s := strings.Map(transform, polymer)
		l := len(react(s))
		if l < smallest {
			smallest = l
		}
	}
	fmt.Println("p2", smallest)
}
