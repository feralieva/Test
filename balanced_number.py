from palindrom import array_int

def is_number_balanced(n):
	arr = array_int(n)
	iter1 = 0
	iter2 = len(arr) - 1
	sum1 = 0
	sum2 = 0
	while iter1 <= len(arr)//2 - 1:
		sum1 = sum1 + arr[iter1]
		iter1 = iter1 + 1
	if len(arr)%2 == 0:
		while iter2 >= len(arr)/2:
			sum2 = sum2 + arr[iter2]
			iter2 = iter2 - 1
	else:
		while iter2 >= len(arr)//2 + 1:
			sum2 = sum2 + arr[iter2]
			iter2 = iter2 - 1
	if sum1 == sum2:
		return True
	else:
		return False

def main():
	print(is_number_balanced(9))
	print(is_number_balanced(11))
	print(is_number_balanced(13))
	print(is_number_balanced(121))
	print(is_number_balanced(4518))
	print(is_number_balanced(28471))
	print(is_number_balanced(1238033))

if __name__ == '__main__':
	main()