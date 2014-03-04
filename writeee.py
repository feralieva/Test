file_name = "TISH.txt"
file = open(file_name,"w")
content = ("python is pretty language! \n the programming is so funny")
file.write(content)
file.close()
print(content)