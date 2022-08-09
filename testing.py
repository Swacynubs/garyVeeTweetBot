#testing.py

#Lets get rid of the numbers at the beginning of the line
newFile = open("newGVQuotes.txt","w", encoding="utf8")
with open("GVQuotes.txt", "r", encoding="utf8") as file:
	for line in file:
		if(line[0]).isdigit():
			string = line.split(" ",1)
			line = string[1]
			newFile.write(line)

		elif line.isspace() == False:
			newFile.write(line)

