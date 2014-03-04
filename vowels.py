def count_vowels(str):
	vow = "aeiouy"
	count = 0

	for item in str:
		for iter in vow:
			if iter == item:
				count = count + 1

	return count

def main():
	print(count_vowels("Hello"))

if __name__ == '__main__':
	main()