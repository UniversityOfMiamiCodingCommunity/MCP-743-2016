#Hepatocyte cell lines

# from os import listdir
# #for x in listdir("..\dataFiles"):
# 	print(x)

class Cells:

	def __init__(self):
		# This is a class variable for storing the name of the cell line.
		# This attributed is derived from the column entitled "Cell Line" in the primary source file. 
		self.nameOfCellLine = ""
		# This is a class variable for indicating if the cells have been transformed.
		self.transformed = ""
		# Leave comment. 
		self.immortalized = ""
		# Leave comment.
		self.immunity = ""
		# Leave comment.
		self.receptor= ""

	def set(self, cellLine, transformed, immortalized, immunity, receptor):

		self.nameOfCellLine = cellLine
		self.transformed = transformed
		self.immortalized = immortalized
		self.immunity = immunity
		self.receptor = receptor

	def printAttributes(self):

		if self.nameOfCellLine:
			print(self.nameOfCellLine, "Cell")#want it to report back cell line name: HepRG, HUH7, etc..
		if self.transformed:
			print("Transformed: ", self.transformed) #want it to report back "yes" or "no"
		if self.immortalized:
			print("Immortalized: ", self.immortalized)#want it to report back "yes" or "no"
		if self.immunity:
			print("Innate Immunity: ", self.immunity) #report back "Fully or Moderatley or Slightly Functional"
		if self.receptor:
			print("HBV Receptor: ", self.receptor) #want it to report back "yes" or "no"
	

fileInput = open("..\dataFiles\HepatocyteCellLines.txt", "r")
i = 0
listOfCellInstances = []
for line in fileInput:
	if i:
		result = line.split("\t")
		#print(result)
		classInstance = Cells()
		classInstance.set(result[0], result[1], result[2], result[3], result[4])
		listOfCellInstances.append(classInstance)
		#classInstance.printAttributes()
	i += 1

for x in listOfCellInstances:
	print x

for x in listOfCellInstances:
	print "------------------------"
	x.printAttributes()
