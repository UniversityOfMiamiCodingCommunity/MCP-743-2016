#Concentration Calculator
############################################################################
def concentrationCalculator (ci, cf, vf):
	answer = (cf*vf)/(ci)
	answer2 = vf - answer
	print("Dilute", answer, "mL of Hygromycin in", answer2, "mL of R10")

concentrationCalculator(50, 0.2, 250)

#Pythagorean Theorem
############################################################################
def pythagoreanTheorem (a, b):
	c = (a**2+b**2)**(1/2)
	print("The length of the third side is", c)

pythagoreanTheorem(3,4)

