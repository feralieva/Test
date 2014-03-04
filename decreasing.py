def is_decreasing(seq):
	iter = 0
	while iter <= len(seq) - 2:
		if seq[iter] <= seq[iter + 1]:
			return False
		else:
			iter = iter + 1
	return True

def main():
	print(is_decreasing([5,4,3,2,1]))
	print(is_decreasing([1,2,3]))
	print(is_decreasing([100, 50, 20]))
	print(is_decreasing([1,1,1,1]))

if __name__ == '__main__':
	main()