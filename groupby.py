def groupby(func, seq):

	d = {}
	for item in seq:
		if func(item) in d:
			d[func(item)] = d[func(item)] + [item]
		else:
			d[func(item)] = [item]

	return d

def main():
	print(groupby(lambda x: x % 2, [0,1,2,3,4,5,6,7]))
	print(groupby(lambda x: 'odd' if x % 2 else 'even', [1, 2, 3, 5, 8, 9, 10, 12]))
	print(groupby(lambda x: x % 3, [0, 1, 2, 3, 4, 5, 6, 7]))

if __name__ == '__main__':
	main()