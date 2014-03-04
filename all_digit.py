from digit_in_number import contains_digit

def contains_digits(number, digits):
	iter = 0
	if digits == []:
		return False
	while iter != len(digits):
		if contains_digit(number, digits[iter]):
			iter = iter + 1
		else:
			return False
	return True

def main():
	print(contains_digits(402123, [0,3,4]))
	print(contains_digits(666, [6,4]))
	print(contains_digits(123456789, [1,2,3,0]))
	print(contains_digits(456, []))

if __name__ == '__main__':
	main()