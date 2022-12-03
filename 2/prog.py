import sys

ROCK = "ROCK"
PAPER = "PAPER"
SCISSORS = "SCISSORS"

MOVE_TABLE = {
	"A": ROCK,
	"B": PAPER,
	"C": SCISSORS,

	"X": ROCK,
	"Y": PAPER,
	"Z": SCISSORS
}

MOVE_SCORE = {
	ROCK: 1,
	PAPER: 2,
	SCISSORS: 3,
}

ROUND_LOST_SCORE = 0
ROUND_DRAW_SCORE = 3
ROUND_WON_SCORE = 6

def execute_round(opponent_move:str, my_move:str):
	if opponent_move == my_move:
		return ROUND_DRAW_SCORE

	if (opponent_move == ROCK) and (my_move == SCISSORS):
		return ROUND_LOST_SCORE

	if (opponent_move == SCISSORS) and (my_move == PAPER):
		return ROUND_LOST_SCORE

	if (opponent_move == PAPER) and (my_move == ROCK):
		return ROUND_LOST_SCORE

	return ROUND_WON_SCORE

def main():
	f = open("input.txt")
	if not f:
		return 1

	score = 0
	for line in f.readlines():
		moves = line.strip().split(" ")
		opponent_move = MOVE_TABLE[moves[0]]
		my_move = MOVE_TABLE[moves[1]]
		score += execute_round(opponent_move, my_move) + MOVE_SCORE[my_move]

	print("Final Score: "+str(score))
	f.close()
	return 0


sys.exit(main())