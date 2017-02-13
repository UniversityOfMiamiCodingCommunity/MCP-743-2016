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