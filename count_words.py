def count_words(arr):
	d = {}
	for item in arr:
		if item in d:   
			d[item] = d[item] + 1
		else:
			d[item] = 1


	return d

def main():
	print(count_words(["apple", "key", "apple"]))
	print(count_words(["apple", "banana", "apple", "pie"]))

if __name__ == '__main__':
	main()
