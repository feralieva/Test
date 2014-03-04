import sys
from random import randint

def generate_numbers(filename, n):
	arr = []
	for item in range(1,n):
		item = randint(1,1000)
		arr = arr + [item]
	contens = str(arr)
	file = open(filename, "w")
	file.write(" ".join(contens))
	file.close()

def main():
	print(generate_numbers(sys.argv[1], int(sys.argv[2])))

if __name__ == '__main__':
    main()