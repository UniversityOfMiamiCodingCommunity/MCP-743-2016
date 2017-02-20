# Assignment 6 Classes
class Element: 
	def __init__(self):
		self.symbol = None 
		self.atomicnumber = None
		self.atomicmass = None 
		self.metalvsnonmetal = None 
	def printAttributes (self): 
		if self.symbol: 
			print("Element symbol:", self.symbol)
		if self.atomicnumber:
			print("Element atomic number:", self.atomicnumber)
		if self.atomicmass: 
			print("Element atomic mass:", self.atomicmass)
		if self.metalvsnonmetal:
			print("Element is:", self.metalvsnonmetal)

elementsodium = Element()
elementsodium.symbol = "Na"
elementsodium.atomicnumber = 11
elementsodium.atomicmass = 22.99
elementsodium.metalvsnonmetal = "Metal"
elementsodium.printAttributes()

elementcalcium = Element()
elementcalcium.symbol = "Ca"
elementcalcium.atomicnumber = 20
elementcalcium.atomicmass = 40.07
elementcalcium.metalvsnonmetal = "Metal"
elementcalcium.printAttributes()

elementneon = Element()
elementneon.symbol = "Ne"
elementneon.atomicnumber = 10
elementneon.atomicmass = 20.18
elementneon.metalvsnonmetal = "Nonmetal"
elementneon.printAttributes()
