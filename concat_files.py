import sys

def main():	
	contents = []
	for i in sys.argv[1:]:

		file1 = open(i, "r")
		content = file1.read()
		contents.append(content)

	concat_file = "MEGATRON.txt"
	file = open(concat_file,"w")
	file.write("\n".join(contents))
	file.close()


if __name__ == '__main__':
	main()
