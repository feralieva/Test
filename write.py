filename = "text.txt"
file = open(filename, "w")
content = ["nqma slunce", "so sad"]
file.write("\n".join(content))
file.close
print(file)
file.close()