def is_increasing(seq):
	iter = 0
	while iter <= len(seq) - 2:
		if seq[iter] >= seq[iter + 1]:
			return False
		else:
			iter = iter + 1
	return True

def main():
	print(is_increasing([1,2,3,4]))
	print(is_increasing([1]))
	print(is_increasing([1,1,1]))
	print(is_increasing([5,6,-10]))
if __name__ == '__main__':
	main()
