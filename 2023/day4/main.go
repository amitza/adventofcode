package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"slices"
	"strings"
)

func calcScore(winNum []string, givenNum []string) int {
	var winCount int
	for _, num := range givenNum {
		if num != "" {
			if slices.Contains(winNum, num) {
				winCount++
			}
		}
	}
	// fmt.Println("win count: ", winCount)
	return int(math.Pow(2, float64(winCount)-1))
}

func parseCard(s string) ([]string, []string) {
	parts := strings.Split(s, ":")
	parts = strings.Split(parts[1], "|")
	winNum := strings.Split(strings.TrimSpace(parts[0]), " ")
	givenNum := strings.Split(strings.TrimSpace(parts[1]), " ")
	// fmt.Println("winning numbers: ", winNum)
	// fmt.Println("numbers: ", givenNum)
	return winNum, givenNum
}

func calcTotalCards(scores []int) int {
	return calcTotalCardsHelper(0, scores, 0)
}

func calcTotalCardsHelper(index int, scores []int, total int) int {
	currentScore := scores[index]
	fmt.Println("index:", index, "current score", currentScore)
	if currentScore == 0 {
		fmt.Println("No Win")
		return 1
	} else {
		var limit int
		if currentScore+1 > len(scores) {
			limit = len(scores)
		} else {
			limit = currentScore + 1
		}
		fmt.Println("index:", index, "Gonna check", limit-(index+1), "more tickets")
		for j := index + 1; j < limit; j++ {
			fmt.Println("Checking ticket:", j)
			total += calcTotalCardsHelper(j, scores, 0)
		}
		// if currentScore > len(scores)-index {
		// 	fmt.Println(currentScore, ">", len(scores)-index)
		// 	return currentScore - index
		// }
	}
	return total
}

func main() {
	filePath := "input_sample.txt"
	file, err := os.Open(filePath)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var totalScore int
	var scores []int
	for scanner.Scan() {
		line := scanner.Text()
		score := calcScore(parseCard(line))
		// fmt.Println("score: ", score)
		totalScore += score
		scores = append(scores, score/2)
	}
	fmt.Println("total score: ", totalScore)
	fmt.Println("n", len(scores), "scores: ", scores)
	fmt.Println("total cards: ", calcTotalCards(scores))
}
