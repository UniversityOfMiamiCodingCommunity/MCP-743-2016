#Katelyn Assignment 6

#Pythagorean Theorem
# a is first side of triangle (in)
###########################

# b is second side of triangle (in)
##############################

#Convert the equation to a python function
##########################################
def pythagoreanTheorem(a, b): #define function
	"""Solve for hypotenuse(c)"""
	c = (a**2 + b**2) ** (0.5)
	print("Hypotenuse result from function:", c, "inches")
	return c #return the result of the function
c = pythagoreanTheorem(3, 4) #use the function one time 


#Kinetic Energy Formula
# m is mass in kilograms
###################

# v is velocity in meters/second
###########################

#Convert the equation to a python function
##########################################
def kineticEnergyFormula(m, v): #define function
	###Solve for Kinetic Energy###
	KE = 0.5 * m * v ** 2 
	print("Kinetic Energy result from function:", KE, "Joules")
	return KE #return the result of the function
KE = kineticEnergyFormula(5, 2) #use the function one time 



