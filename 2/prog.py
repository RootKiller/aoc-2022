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

OUTCOME_LOSE = "LOSE"
OUTCOME_DRAW = "DRAW"
OUTCOME_WIN = "WIN"
OUTCOME_TABLE = {
	"X": OUTCOME_LOSE,
	"Y": OUTCOME_DRAW,
	"Z": OUTCOME_WIN
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

def determine_move(opponent_move: str, desired_outcome: str):
	if desired_outcome == OUTCOME_DRAW:
		return opponent_move

	if desired_outcome == OUTCOME_WIN:
		if opponent_move == ROCK:
			return PAPER
		if opponent_move == PAPER:
			return SCISSORS
		if opponent_move == SCISSORS:
			return ROCK
	if desired_outcome == OUTCOME_LOSE:
		if opponent_move == ROCK:
			return SCISSORS
		if opponent_move == PAPER:
			return ROCK
		if opponent_move == SCISSORS:
			return PAPER

	return SCISSORS


def part_one(lines):
	score = 0
	for line in lines:
		moves = line.strip().split(" ")
		opponent_move = MOVE_TABLE[moves[0]]
		my_move = MOVE_TABLE[moves[1]]
		score += execute_round(opponent_move, my_move) + MOVE_SCORE[my_move]

	print("Part 1 - Final Score: "+str(score))

def part_two(lines):
	score = 0
	for line in lines:
		data = line.strip().split(" ")
		opponent_move = MOVE_TABLE[data[0]]
		outcome = OUTCOME_TABLE[data[1]]

		my_move = determine_move(opponent_move, outcome)

		score += execute_round(opponent_move, my_move) + MOVE_SCORE[my_move]

	print("Part 2 - Final Score: "+str(score))

def main():
	f = open("input.txt")
	if not f:
		return 1

	lines = f.readlines()
	part_one(lines)
	part_two(lines)

	f.close()
	return 0


sys.exit(main())