def prepare_meal(number):
	arr = []
	if number % 3 != 0:
		arr = arr + ['']
	while number % 3 == 0:
		number = number//3
		arr = arr + ['spam']
	return arr
def main():
	print(prepare_meal(27))
	print(prepare_meal(7))
if __name__ == '__main__':
	main()