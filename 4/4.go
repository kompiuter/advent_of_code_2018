package main

import (
	"fmt"
	"io/ioutil"
	"sort"
	"strconv"
	"strings"
)

func getTime(s string) int {
	t, err := strconv.Atoi(s[15:17])
	if err != nil {
		panic(err)
	}
	return t
}

func maxInts(a []int) int {
	if len(a) == 0 {
		return 0
	}
	if len(a) == 1 {
		return a[0]
	}
	max := a[0]
	for _, v := range a[1:] {
		if v > max {
			max = v
		}
	}
	return max
}

func indexOfSlice(x int, a []int) int {
	for i := range a {
		if a[i] == x {
			return i
		}
	}
	return -1
}

func readLines(file string) []string {
	b, err := ioutil.ReadFile(file)
	if err != nil {
		panic(err)
	}

	return strings.Split(string(b), "\n")
}

func main() {
	sd := make(map[int]int)
	md := make(map[int][]int)
	var guard int
	var sleepTime int
	input := readLines("input.txt")
	sort.Strings(input)

	for _, line := range input {
		if strings.Contains(line, "Guard") {
			guardStr := strings.Split(line, " ")[3][1:]
			guard, _ = strconv.Atoi(guardStr)
		} else if strings.Contains(line, "falls") {
			sleepTime = getTime(line)
		} else {
			time := getTime(line)
			sd[guard] += (time - sleepTime)
			if md[guard] == nil {
				md[guard] = make([]int, 60)
			}
			for i := sleepTime; i < time; i++ {
				md[guard][i]++
			}
		}
	}

	lazyGuard := 0
	for k, v := range sd {
		if v > sd[lazyGuard] {
			lazyGuard = k
		}
	}

	bestMin := -1
	lazyMin := 0
	for i, v := range md[lazyGuard] {
		if v > bestMin {
			bestMin = v
			lazyMin = i
		}
	}
	fmt.Println(lazyGuard * lazyMin)

	bestMin = -1
	for guard, mins := range md {
		maxMin := maxInts(mins)
		if maxMin > bestMin {
			bestMin = maxMin
			lazyMin = indexOfSlice(bestMin, mins)
			lazyGuard = guard
		}
	}
	fmt.Println(lazyGuard * lazyMin)
}
