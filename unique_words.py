def unique_words_count(arr):
	d = {}
	for item in arr:
		if item in d:
			d[item] = d[item] + 1
		else:
			d[item] = 1

	return len(d)

def main():
	print(unique_words_count(["python", "python", "python", "ruby"]))
	print(unique_words_count(["HELLO!"] * 10))
	print(unique_words_count(["apple", "banana", "apple", "pie"]))

if __name__ == '__main__':
	main()
