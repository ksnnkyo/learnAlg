package main

import "fmt"

func quick(quickList []int) []int {
	listLen := len(quickList)
	if listLen >= 2 {
		mid := quickList[0]
		var left, right, result []int
		for i := 1; i < listLen; i++ {
			if quickList[i] > mid {
				right = append(right, quickList[i])
			} else {
				left = append(left, quickList[i])
			}
		}
		result = append(result, quick(left)...)
		result = append(result, mid)
		result = append(result, quick(right)...)
		return result
	}

	return quickList
}

func main() {
	quickList := []int{3, 4, 1, 2, 5, 8, 0}
	fmt.Println(quick(quickList))
}
