# Date: 2017.01.28
###################

# When you are stuck or need to explore something new start here:
# https://docs.python.org/3/tutorial/
# Also, Stackoverflow is a great resource: 
# http://stackoverflow.com
#################################################################

############################################################################################################
# Throughout these tutorials, you may have to add your own print statements to see the results of the code.
############################################################################################################

#################################################################################
# Numbers
# If you need help or need to explore something new regarding numbers start here:
# https://docs.python.org/3/tutorial/introduction.html#numbers
#################################################################################

# In Python a variable is assigned using the "=" sign (e.g. a = 1 below).
# There are two primary number types in Python:
#########################################################################

# 1) Integers: all whole numbers (i.e. no decimal points)
##########################################################################
a = 1
b = 2

# The usual mathematical operations are available for integers. 
###############################################################
answer1 = a + b
answer2 = a - b
answer3 = a * b
answer4 = a / b

# You don't need to have spaces bewteen operators and numbers, but spaces help with readability. 
# For example, these expressions give equivalent answers to those above. 
################################################################################################
answer1 = a+b
answer2 = a-b
answer3 = a*b
answer4 = a/b

# 2) Floats: floating point numbers (i.e. numbers with decimal values)
######################################################################
a = 1.0
b = 2.0

# The usual mathematical operations are available for floats. 
#############################################################
answer1 = a + b
answer2 = a - b
answer3 = a * b
answer4 = a / b

# There is an operator for floats that you may not be familiar with called the modulo (%).
# It returns the remainder of a division operation.
###########################################################################################
answer5 = a % b # remainder is 1.0
b = 1.0
answer6 = a % b # now that we reassigned the variable b, the remainder is 0

#############################################################
# There are other, infrequently used operators for floats.
# For a full list explore the links at the top of this page. 
#############################################################

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
<<<<<<< HEAD
print("Volume:", v, "liters") 

print("\n")


###################################
# Start of ZPR assignment, numbers.
###################################

# Einstein's formula for energy


# Mass of a hydrogen atom (kg)
#######################################################################
m = ((1.6737236*10)**(-27)) 

# Constant for the speed of light (m/s)
#######################################################################
c = 299792458 

# Solve for energy (E)
#######################################################################
E = m*(c**2)

# Print the results to the screen
#######################################################################
print("Energy:", E, "joules")


print("\n")

# Growth formula for bacteria


# P is a variable but stands for the number of initial bacteria
#######################################################################
P = 2000

# e is a mathematical constant 
#######################################################################
e = 2.71828

# t is a variable for the time that the bacteria is allowed to grow (hours)
#######################################################################
t = 6

# k is a varible, referred to as the growth constant (doubling/hour)
#######################################################################
k = 0.25

# Solve for final amount of bacteria (A)
#######################################################################
A = P*(e**(k*t))

# Print the results to screen
#######################################################################
print("Final amount of bacteria:", A, "bacteria")

