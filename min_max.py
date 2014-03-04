def sum_of_min_and_max(arr):
	min = arr[0]
	max = arr[0]

	for item in arr:
		if item < min:
			min = item
		if item > max:
			max = item

	sum = min + max
	return sum

def main():
	print(sum_of_min_and_max([1,2,3]))
	print(sum_of_min_and_max([1,2,3,4,5,6,8,9]))
	print(sum_of_min_and_max([-10,5,10,100]))
	print(sum_of_min_and_max([1]))

if __name__ == '__main__':
	main()
