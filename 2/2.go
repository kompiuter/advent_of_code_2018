package main

import (
	"bufio"
	"fmt"
	"os"
)

func readLines(path string) ([]string, error) {
	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines, scanner.Err()
}

func runeCount(s string) map[rune]int {
	m := make(map[rune]int)
	for _, rune := range s {
		m[rune] += 1
	}
	return m
}

func main() {
	ids, err := readLines("input.txt")
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	twos, threes := 0, 0
	for _, id := range ids {
		twoFound, threeFound := false, false
		m := runeCount(id)
		for _, v := range m {
			if v == 2 && !twoFound {
				twos++
				twoFound = true
			}
			if v == 3 && !threeFound {
				threes++
				threeFound = true
			}
		}
	}

	fmt.Println(twos * threes)

loop:
	for i := 0; i < len(ids)-1; i++ {
		for j := i + 1; j < len(ids); j++ {
			numDiffs := 0
			lastDiffIdx := -1
			for k := 0; k < len(ids[i]); k++ {
				if ids[i][k] != ids[j][k] {
					numDiffs++
					lastDiffIdx = k
				}
			}
			if numDiffs == 1 {
				s := ids[i]
				s = s[:lastDiffIdx] + s[lastDiffIdx+1:]
				fmt.Println(s)
				break loop
			}
		}
	}
}
