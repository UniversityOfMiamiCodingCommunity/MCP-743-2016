#Hepatocyte cell lines

from os import listdir
for x in listdir("..\dataFiles"):
	print(x)

fileInput = open("..\dataFiles\HepatocyteCellLines.txt", "r")
Cell = ""
for line in fileInput:
	result = line.split("\t")
	print(result)
	#~ Cell += line[0:-1]
#~ print(Cell)

#x.split("\t")

class Cells:

	def __init__(self):
		self.name = "Cell Line"
		self.growth = "Transformed"
		self.lifespan = "Immortilized"
		self. response = "Innate Immunity"
		self.receptor= "HBV Receptor"
	def printAttributes(self):

		if self.name:
			print(self.name, "Cell")#want it to report back cell line name: HepRG, HUH7, etc..
		if self.growth:
			print("Transformed: ", self.growth) #want it to report back "yes" or "no"
		if self.lifespan:
			print("Immortalized: ", self.lifespan)#want it to report back "yes" or "no"
		if self.response:
			print("Innate Immunity: ", self.response) #report back "Fully or Moderatley or Slightly Functional"
		if self.receptor:
			print("HBV Receptor: ", self.receptor) #want it to report back "yes" or "no"
	
	

#~ Hepatocyte = Cell ()
#~ # Populate the attributes of the class 
#~ One.name = 
#~ One.growth = 
#~ One.lifespan = 
#~ One.response =
#~ One.receptor = 
#~ One.printAttributes()
