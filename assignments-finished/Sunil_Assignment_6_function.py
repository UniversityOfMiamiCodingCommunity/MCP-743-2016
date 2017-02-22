#Equation of Choice 1: Newton's Law
def get_force(m,a,sig_figs=2):
	print("Note:\nThe get_force function takes mass and acceleration as the first and second argument respectively.\nAn optional third arguments takes the number of significant figures if specified, the default being 2.\n")
	force=m*a
	print("The force appled to the body is: "+str(round(force,sig_figs))+" Newtons")
get_force(0.333333,10,3)
#The third argument was set to 3 significant numbers
###################################################################################################
print("\n\n\n")
###################################################################################################
#Equation of Choice 2: Heat Capacity
def get_energy(m,s,i,f,sig_figs=2):
	print("Note:\nThe get_energy function takes the following order of arguments:\n1st Argument: Mass\n2nd Argument: Specific Heat\n3rd Argument: Initial Temperature\n4th Argument: Final Temperature\n5th Argument: Number of Significant Digits (Optional, Default being 2).\n")
	energy=m*s*(f-i)
	print("The Energy supplied to the body is: "+str(round(energy,sig_figs))+" Joules")
get_energy(300.0,2.44,10.0,30.0) 
#The fifth argument is 2 by default
##################################################################################################
