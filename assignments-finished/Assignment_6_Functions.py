#Assignment - 6 - Functions
###########################

###-------> Originial Equations

#Test Equation.
###############
n = 1
m = 2
p = 10
x = p/(m*n)
print(x)


# Equation 1 - Circumfrence of a Sphere
#######################################

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



# Equation 3 - Quadratic Equation
#################################

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



###--------> Equations as Functions



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



#Turning Equations 1 into a function
####################################

r = 12
pi = 3.14
C = 2*(pi)*r

def CircumfrenceEquation(r, pi):
	C = 2*(pi)*r
	print(C)
	return C

C = CircumfrenceEquation(12, 3.14)


#Turning Equation 2 into a function
###################################

C = 37
F = C * (9/5) + 32

def CelciusToFarenheit(C):
	F = C * (9/5) + 32
	print(F)
	return F

F = CelciusToFarenheit(37)


#Turning Equation 3 into a function
###################################

a = 2
b = 2
c = 2
x = (-b + (b**2-4*a*c)**0.5)/2*a
x = (-b - (b**2-4*a*c)**0.5)/2*a

def QuadraticEquationPLUS(a, b, c):
	x = (-b + (b**2-4*a*c)**0.5)/2*a
	print(x)
	return x

x = QuadraticEquationPLUS(2, 2, 2)

def QuadraticEquationMINUS(a, b, c):
	x = (-b - (b**2-4*a*c)**0.5)/2*a
	print(x)
	return x

x = QuadraticEquationMINUS(2, 2, 2)
