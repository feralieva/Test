from is_prime import is_prime

def devisors(n):
	iter = 1
	dev = 0
	while iter <= n:
		if n%iter == 0:
			dev = dev + 1
		iter = iter + 1

	return dev

def prime_number_of_devisors(n):
	if is_prime(devisors(n)):
		return True
	return False

def main():
	print(prime_number_of_devisors(8))
	print(prime_number_of_devisors(7))

if __name__ == '__main__':
	main()
