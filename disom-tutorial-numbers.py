<<<<<<< HEAD
## Date: 2017.01.28
=======
# Date: 2017.01.28
>>>>>>> refs/remotes/origin/master
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
 
###########################
# Nick's numbers assignment
###########################

# Converting between relative centrifugal force, RCF, and rotations per minute, RPM.
####################################################################################

# Variable for radius of the rotor in centimeters
###########################################################
r = 14.0 

# Variable for the speed at which the rotor is spinning in RPM
##############################################################
RPM = 12000.0

# Constant for angular acceleration
###################################
c = 1.118 * 10**-5

# Solving for RCF, measured in times gravity:
#############################################
RCF = c * r * RPM**2
RCF = round(RCF, 2)

print("Relative Centrifugal Force:", RCF, "g's")
################################################

# Converting temperature from Fahrenheit to Celsius or Kelvin
#############################################################

# Variable for temperature in Fahrenheit 
########################################
Tf = 80.0

# Solving for temperature in Celsius
####################################
Tc = Tf - 32 * 5 / 9
Tc = round(Tc, 2)

print("Temperature in Celsius:", Tc, "degrees")

# Solving for temperature in Kelvin
###################################
Tk = (Tc + 273.15)
Tk = round(Tk, 2)

print("Temperature in Kelvin:", Tk)

=======
print("Volume:", v, "liters") 
>>>>>>> refs/remotes/origin/master
