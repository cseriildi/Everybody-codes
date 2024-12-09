def parse(filename):
	with open(filename, "r") as infile:
		words, text = infile.read().split("\n\n")
		return words[6:].split(","), text
	

def part1(input):
	words, text = input

	return sum(text.count(word) for word in words)

def part2(input):
	words, text = input
	words += [word[::-1] for word in words]
	indexes = set()
	for word in words:
		found_at = text.find(word)
		while found_at != -1:
			for i in range(len(word)):
				indexes.add(found_at + i)
			found_at = text.find(word, found_at + 1)
	return len(indexes)


def part3(input):

	words, text = input
	text = text.splitlines()
	words += [word[::-1] for word in words]
	rows = len(text)
	cols = len(text[0])

	indexes = set()

	for i in range(rows):
		for j in range(cols):
			for word in words:
				word_len = len(word)
				#vertical check
				if i + word_len <= rows and all(text[i + x][j] == word[x] for x in range(word_len)):
					for x in range(word_len):
						indexes.add((i + x, j))
				#horizontal check
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
