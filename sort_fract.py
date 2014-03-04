def sort_fractions(fractions):
	frac = sorted(fractions, key = lambda a: -a[1])
	return frac
		
def main():
	print(sort_fractions([(2, 3), (1, 2), (1, 3)]))

if __name__ == '__main__':
	main()