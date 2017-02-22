####################################################################
# Assignment
# Code two scientific equations of your choosing in Python.
# Make sure the equations are fully commented. See my example below.
####################################################################

# Example: Ideal Gas Law
# Note: usually the numbers in scientifc equations are floats, so code them as such.
# For example, below I have 1.0 mole, not 1 mole. 
####################################################################################

# Variable for pressure in units of Pascal (1 atm = 101325.0 Pascal).
#####################################################################
p = 101325.0 

# Variable for number of moles of gas molecules.
################################################
n = 1.0

# Ideal gas constant in units J/(K mol).
########################################
R = 8.314

# Variable for temperature in units of Kelvin.
##############################################
T = 298.0

# Solve for volume.
###################
v = (n*R*T)/p

# Print the results to the screen.
##################################
print("Volume:", v, "liters") 

##################################

#Test Equation.
###############
n = 1
m = 2
p = 10
x = p/(m*n)
print(x)

# Equation 1 - Circumfrence of a Sphere

#Radius of the Circle (inches)
r = 12

#Pi
pi = 3.14

#Solve for Circumfrence C (inches)
C = 2*(pi)*r

#Print Results
print("Circumfrence:", C, "inches")


# Equation 2 - Converting degrees Celcius to degrees Farenheit
##############################################################

# Degrees Celcius
C = 37

#Solve for Farenheit (F) in degrees
F = C * (9/5) + 32

#Print Results
print(F, "degrees Farenheit")


#Equation 3 - Quadratic Equation


#
a = 2

#
b = 2

#
c = 2

#Solve for x (+)
x = (-b + (b**2-4*a*c)**0.5)/2*a
print(x)


#Solve for x (-)
x = (-b - (b**2-4*a*c)**0.5)/2*a
print(x)


#Turning Test Equation into a function
######################################

n = 1
m = 2
p = 10
x = p/(m*n)

def TestEquation(n, m, p):
	x = p/(m*n)
	print(x)
	return x

x = TestEquation(1, 2, 10)





