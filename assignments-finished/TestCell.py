#Hepatocyte cell lines

from os import listdir
for x in listdir("..\dataFiles"):
	print(x)

fileInput = open("..\dataFiles\HepatocyteCellLines.txt", "r")
Cell = ""
for line in fileInput:
	if line[0]== ">":
		continue
	Cell += line[0:-1]
print(Cell)


