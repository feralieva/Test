def count_substrings(haystack, needle):
	i = 0
	j = 0
	count = 0
	while i <= len(haystack) - 1:
		if haystack[i] == needle[j]:
			i = i + 1
			j = j + 1
			if j == len(needle):
				count = count + 1
				j = 0
		else:
				i = i + 1

	return count

def main():
	print(count_substrings("This is a test string", "is"))
	print(count_substrings("babababa", "baba"))
	print(count_substrings("Python is an awesome language to program in!", "o"))
	print(count_substrings("We have nothing in common!", "really?"))
	print(count_substrings("This is this", "this"))

if __name__ == '__main__':
	main()