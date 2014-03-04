from all_divisors import sum_of_divisors

def is_prime(n):
	if sum_of_divisors(n) == 1 + n:
		return True
	return False

def main():
	print(is_prime(4))
	print(is_prime(-10))
	print(is_prime(2))

if __name__ == '__main__':
	main()