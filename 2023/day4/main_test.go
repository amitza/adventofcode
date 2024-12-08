package main

import "testing"

func TestValidScore(t *testing.T) {
	card := "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19"
	w, g := parseCard(card)
	score := calcScore(w, g)
	if score != 2 {
		t.Fatal("Expected different score:", score)
	}
}
