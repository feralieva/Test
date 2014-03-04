def gcd(a,b):
	while b != 0:
		(a, b) = (b, a%b)
	return a

def simplify_fraction(fraction):
	digit = list(fraction)
	g = gcd(digit[0], digit[1])
	digit[0] = digit[0]//g
	digit[1] = digit[1]//g
	fraction = tuple(digit)
	return fraction

def main():
	print(simplify_fraction((2,4)))
	print(simplify_fraction((63,462)))
	
if __name__ == '__main__':
	main()