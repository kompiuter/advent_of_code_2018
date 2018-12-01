package main

import (
	"fmt"
	"io"
	"os"
)

func readInts(filename string) ([]int, error) {
	f, err := os.Open(filename)
	if err != nil {
		return nil, fmt.Errorf("could not open %s: %v", filename, err)
	}

	var n int
	var nums []int
	for {
		_, err := fmt.Fscanf(f, "%d\n", &n)
		if err != nil {
			if err == io.EOF {
				break
			}
			return nil, fmt.Errorf("could not scan file: %v", err)
		}
		nums = append(nums, n)
	}
	return nums, nil
}

func main() {
	nums, err := readInts("input.txt")
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	sum := 0
	for _, n := range nums {
		sum += n
	}
	fmt.Printf("resulting frequency: %d\n", sum)

	sum = 0
	seen := make(map[int]bool)
loop:
	for {
		for _, n := range nums {
			sum += n
			if _, found := seen[sum]; found {
				fmt.Printf("first frequency reached twice: %d\n", sum)
				break loop
			}
			seen[sum] = true
		}
	}
}
