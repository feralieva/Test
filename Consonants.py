def count_consonants(str):
	consonants = "bcdfghjklmnqrstvwxz"
	count = 0

	for iter in str:
		for item in consonants:
			if iter == item:
				count = count + 1
	return count

def main():
	print(count_consonants("choise"))

if __name__ == '__main__':
	main()