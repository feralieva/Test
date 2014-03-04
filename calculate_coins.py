def calculate_coins(sum):
	coins = [100, 50, 20, 10, 5, 2, 1]
	d = {}
	sum = int(sum * 100)
	for item in coins:
		if item in d:
			if sum >= item:
				sum = sum - item
				d[item] = d[item] + 1
		else:
			if sum >= item:
				sum = sum - item
				d[item] = 1
			else:
				d[item] = 0

	return d

def main():
	print(calculate_coins(0.53))
	#{1: 1, 2: 1, 100: 0, 5: 0, 10: 0, 50: 1, 20: 0}
	print(calculate_coins(8.94))
	#{1: 0, 2: 2, 100: 8, 5: 0, 10: 0, 50: 1, 20: 2}

if __name__ == '__main__':
	main()
	
