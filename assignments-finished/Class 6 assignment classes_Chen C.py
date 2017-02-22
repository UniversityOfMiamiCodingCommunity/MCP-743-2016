# When you are stuck or need to explore something new start here:
# https://docs.python.org/3/tutorial/
# Also, Stackoverflow is a great resource: 
# http://stackoverflow.com
#################################################################
# Classes (also known as objects)
# If you need help or need to explore something new regarding classes start here: https://docs.python.org/3/tutorial/classes.html
##################################################################################################################################
# Class 6 Assignment
# 2)Create a class for something. It would be nice if the class were science-related. The class should contain attributes and at least one class method (i.e. function). See my Cars class as an example.
# 3)Create three different instances of your class
##################################################################################################################################
class Sts5Mutants: 

	def __init__(self):
		self.CellLength = None 
		self.CellWidth = None
		self.Rad24Binding = None
		self.Longevity = None

	def printAttributes(self):

		if self.CellLength:
			print("Cell Length:", self.CellLength)
		if self.CellWidth:
			print("Cell Width:", self.CellWidth)
		if self.Rad24Binding:
			print("Rad24 Binding:", self.Rad24Binding)
		if self.Longevity:
			print("Longevity", self.Longevity)

Sts5WT = Sts5Mutants()
Sts5WT.CellLength = 14
Sts5WT.CellWidth = 4.4
Sts5WT.Rad24Binding = 1
Sts5WT.Longevity = "Normal"
Sts5WT.printAttributes()

Sts5A = Sts5Mutants()
Sts5A.CellLength = 12
Sts5A.CellWidth = 4.6
Sts5A.Rad24Binding = 0.4
Sts5A.Longevity = "Increased"
Sts5A.printAttributes()

Sts5D = Sts5Mutants()
Sts5D.CellLength = 15
Sts5D.CellWidth = 4.2
Sts5D.Rad24Binding = 1.5
Sts5D.Longevity = "Decreased"
Sts5D.printAttributes()


