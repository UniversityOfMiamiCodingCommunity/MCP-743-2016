# Date: 2017.02.22
###################


#####################################
# Start of ZPR assignment, functions.
#####################################

# Einstein's formula for energy


# Mass of a hydrogen atom (kg)
#######################################################################
mass_of_hydrogen_atom = ((1.6737236*10)**(-27)) 

# Constant for the speed of light (m/s)
#######################################################################
speed_of_light = 299792458 

#######################################################################
def einsteinsEquation(m, c):
	
	# Solve for Energy
	##################
	E = m*(c**2)
	print("Energy result from function:", E, "joules")
	return E
	
E = einsteinsEquation(mass_of_hydrogen_atom, speed_of_light)


print("\n")

#~ # Growth formula for bacteria
#~ ########################################################################

# p is a variable but stands for the number of initial bacteria
#####################################################################
initialBacteria = 2000

# e is a mathematical constant 
#####################################################################
e_mathConstant = 2.71828

# t is a variable for the time that the bacteria is allowed to grow (hours)
#####################################################################
growthTime = 6

# k is a varible, referred to as the growth constant (doubling/hour)
#####################################################################
growthConstant = 0.25

#~ # Solve for final amount of bacteria (A)
#~ #####################################################################
#~ A = P*(e**(k*t))

#~ # Print the results to screen
#~ #####################################################################
#~ print("Final amount of bacteria:", A, "bacteria")

def bacterialGrowthFormula(p, e, t, k):
	
	# Solve for final amount of bacteria
	####################################
	A = p*(e**(k*t))
	print("Amount result from function:", A, "bacteria")
	return A
	
A = bacterialGrowthFormula(initialBacteria, e_mathConstant, growthTime, growthConstant)
 
	 


