def sevens_in_a_row(arr, n):
	sevens = 0
	is_sevens = False
	for item in arr:
		if item == 7:
			sevens = sevens + 1
		else:
			if n == sevens:
				is_sevens = True
				return True
			sevens = 0
	return is_sevens

def main():
	print(sevens_in_a_row([1,7,7,1,4,7], 2))
	print(sevens_in_a_row([1,7,1,7,7], 4))

if __name__ == '__main__':
	main()