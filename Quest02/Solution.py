def parse(filename):
	with open(filename, "r") as infile:
		words = infile.readline().strip("\n").replace("WORDS:", "").split(",")
		infile.readline()
		text = infile.read()
		return words, text

def part1():
	words, text = parse("part1_input.txt")

	return sum(text.count(word) for word in words)

def part2():
	words, text = parse("part2_input.txt")
	words += [word[::-1] for word in words]
	indexes = set()
	for word in words:
		found_at = text.find(word)
		while found_at != -1:
			for i in range(len(word)):
				indexes.add(found_at + i)
			found_at = text.find(word, found_at + 1)
	return len(indexes)

def part3(): 


	return 

if __name__ == "__main__":
	print("Solution for Part 1: ", part1())
	print("Solution for Part 2: ", part2())
	print("Solution for Part 3: ", part3())