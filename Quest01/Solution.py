def parse(filename):
	with open(filename, "r") as infile:
		return infile.readline()
	
def get_potions(type):

	type = type.replace("x", "")
	participants = len(type)	
	potions = {"A": 0, "B": 1, "C": 3, "D": 5}

	return sum(potions[i] for i in type) + participants * (participants - 1)

def part1():
	input = parse("part1_input.txt")
	return sum(get_potions(enemy) for enemy in input)

def part2():
	input = parse("part2_input.txt")
	input = [input[i:i + 2] for i in range(0, len(input), 2)]

	return sum(get_potions(pair) for pair in input)

def part3():
	input = parse("part3_input.txt")
	input = [input[i:i + 3] for i in range(0, len(input), 3)]

	return sum(get_potions(group) for group in input)

if __name__ == "__main__":
	print("Solution for Part 1: ", part1())
	print("Solution for Part 2: ", part2())
	print("Solution for Part 3: ", part3())