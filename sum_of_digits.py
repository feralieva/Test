def sum_of_digits(n):
	sum = 0
	n = abs(n)

	while n != 0:
		sum = sum + n%10
		n = n//10

	return sum

def main():
	print (sum_of_digits(34))
	print (sum_of_digits(-34))

if __name__ == '__main__':
	main()
