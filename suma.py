import sys

def main():
	filename=sys.argv[1]
	sum = 0
	file = open(filename,"r")
	content = file.read()
	for i in content:
		sum += int(i)
	print(content)

if __name__ == '__main__':
	main()