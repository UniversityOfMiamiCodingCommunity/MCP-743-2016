def quadsolver(a, b, c) :
	if b**2 - 4 * a *c < 0 :
		print("Error, equation had imaginary roots")
	if b**2 - 4 * a *c >= 0 :
		x1 = (- b + ((b**2 - 4 * a *c)**0.5)) / (2 * a)
		x2 = (- b - ((b**2 - 4 * a *c)**0.5)) / (2 * a)
		print("The roots of the quadratic are ",x1,"and ",x2,".")
		return x1
		return x2

a = 4
b = 10
c = 1
quadsolver(a, b, c)


def slopecalc(P1, P2) :
	u1 = int(P1[1:2])
	u2 = int(P1[4:5])
	v1 = int(P2[1:2])
	v2 = int(P2[4:5])
	slop = ((v2 - v1)/(u2 - u1))
	print("The slope is ",slop,".")
	return slop
P1 = "(2, 3)"
P2 = "(4, 8)"
slopecalc(P1, P2)

class Chemicals:

	def __init__(self):

		self.name = None
		self.formula = None
		self.MW = None
		self.density = None
		self.state = None

	def printAttributes(self):

		if self.name:
			print("Name of chemical:", self.name)
		if self.formula:
			print("Molecular formula:", self.formula)
		if self.MW:
			print("Molecular weight:", self.MW)
		if self.density:
			print("Density:", self.density)
		if self.state:
			print("State of matter:", self.state)

chemical1 = Chemicals()
chemical1.name = "Ethanol"
chemical1.formula = "C2H5OH"
chemical1.MW = "46.07 g/mol"
chemical1.density = "0.7893 g/cm^3"
chemical1.state = "liquid"
chemical1.printAttributes()

chemical2 = Chemicals()
chemical2.name = "Acetone"
chemical2.formula = "(CH3)2O"
chemical2.MW = "58.08 g/mol"
chemical2.density = "0.7854 g/cm^3"
chemical2.state = "liquid"
chemical2.printAttributes()

chemical3 = Chemicals()
chemical3.name = "Argon"
chemical3.formula = "Ar"
chemical3.MW = "39.948 g.mol"
chemical3.density = "1.784 g/L"
chemical3.state = "gas"
chemical3.printAttributes()



