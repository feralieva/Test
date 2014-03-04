from palindrom import array_int

def contains_digit(number, digit):
	arr = array_int(number)
	for item in arr:
		if item == digit:
			return True
	return False

def main():
	print(contains_digit(1234, 5))
	print(contains_digit(12346789, 5))
	print(contains_digit(1000, 0))

if __name__ == '__main__':
	main()
