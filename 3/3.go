package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"regexp"
	"strconv"
	"strings"
)

var claimRegex = regexp.MustCompile(`\A#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)\z`)

type claim struct {
	id   int
	left int
	top  int
	wide int
	tall int
}

func (c claim) String() string {
	return fmt.Sprintf("id: %d, left: %d, top: %d, wide: %d, tall: %d",
		c.id, c.left, c.top, c.wide, c.tall)
}

func newClaim(claimStr string) (*claim, error) {
	groups := claimRegex.FindAllStringSubmatch(claimStr, -1)
	var res []int
	for i, s := range groups[0] {
		if i == 0 {
			continue
		}
		n, err := strconv.Atoi(s)
		if err != nil {
			return nil, err
		}
		res = append(res, n)
	}
	return &claim{
		id:   res[0],
		left: res[1],
		top:  res[2],
		wide: res[3],
		tall: res[4],
	}, nil
}

type fabric struct {
	width           int
	height          int
	canvas          []int
	claims          map[int][]int
	overlappedCells int
}

func newFabric(width, height int) *fabric {
	return &fabric{
		width,
		height,
		make([]int, width*height),
		make(map[int][]int),
		0,
	}
}

func (f *fabric) addClaim(c claim) {
	cells := f.getClaimCells(c)
	for _, cell := range cells {
		f.canvas[cell]++
		if f.canvas[cell] == 2 {
			f.overlappedCells++
		}
	}
	f.claims[c.id] = cells
}

func (f *fabric) getClaimCells(c claim) []int {
	var cells []int
	for i := 0; i < c.tall; i++ {
		curHeight := f.height * (c.top + i)
		rowStart := curHeight + c.left
		rowEnd := rowStart + c.wide
		for cell := rowStart; cell < rowEnd; cell++ {
			cells = append(cells, cell)
		}
	}
	return cells
}

func (f *fabric) disjointClaimID() int {
	for claimID, cells := range f.claims {
		found := true
		for _, cell := range cells {
			if f.canvas[cell] > 1 {
				found = false
				break
			}
		}
		if found {
			return claimID
		}
	}
	return -1
}

func main() {
	b, err := ioutil.ReadFile("input.txt")
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	const fabricSize = 1000
	f := newFabric(fabricSize, fabricSize)
	claims := strings.Split(string(b), "\n")
	for _, claimStr := range claims {
		claim, err := newClaim(claimStr)
		if err != nil {
			fmt.Printf("could not create claim from str: %v", err)
			os.Exit(1)
		}
		f.addClaim(*claim)
	}

	fmt.Printf("overlapping cells: %d\n", f.overlappedCells)
	fmt.Printf("disjoint claim id: %d\n", f.disjointClaimID())
}
