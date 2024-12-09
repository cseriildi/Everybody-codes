def parse(filename):
	with open(filename, "r") as infile:
		words, text = infile.read().split("\n\n")
		words = words[6:].split(",")
		text = text.splitlines()
		return words, text
	
def part1(input):
	return 

def part2(input):
	

	return

def part3(input):

	words, text = input
	words += [word[::-1] for word in words]
	rows = len(text)
	cols = len(text[0])

	indexes = set()

	for i in range(rows):
		for j in range(cols):
			for word in words:
				word_len = len(word)
				if i + word_len <= rows and all(text[i + x][j] == word[x] for x in range(word_len)):
					for x in range(word_len):
						indexes.add((i + x, j))

				line = text[i] * 2
				if word_len <= cols and line[j : j + word_len] == word:
					for x in range(word_len):
						indexes.add((i, (j + x) % cols))
	return len(indexes)


if __name__ == "__main__":
	input = parse("part1_input.txt")
	example = parse("part1_example.txt")
	print("Example for Part 1: ", part1(example))
	print("Solution for Part 1: ", part1(input))

	input = parse("part2_input.txt")
	example = parse("part2_example.txt")
	print("Example for Part 2: ", part2(example))
	print("Solution for Part 2: ", part2(input))

	input = parse("part3_input.txt")
	example = parse("part3_example.txt")
	print("Example for Part 3: ", part3(example))
	print("Solution for Part 3: ", part3(input))