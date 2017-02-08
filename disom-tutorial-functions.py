# When you are stuck or need to explore something new start here:
# https://docs.python.org/3/tutorial/
# Also, Stackoverflow is a great resource: 
# http://stackoverflow.com
#################################################################

############################################################################################################
# Throughout these tutorials, you may have to add your own print statements to see the results of the code.
############################################################################################################

#########################################################
# My equation for the Ideal Gas Law from classes 1 and 2.
#########################################################

# Variable for pressure in units of Pascal (1 atm = 101325.0 Pascal).
#####################################################################
pressure = 101325.0 

# Variable for number of moles of gas molecules.
################################################
moles = 1.0

# Ideal gas constant in units J/(K mol).
########################################
gasConstant = 8.314

# Variable for temperature in units of Kelvin.
##############################################
temperature = 298.0

# Solve for volume.
###################
v = (moles*gasConstant*temperature)/pressure

# Print the results to the screen.
##################################
print("Volume:", v, "liters") 

#########################################################
# Convert the equation to a Python function.
#########################################################

def idealGasLaw(p, n, R, T): # define function

	# Solve for volume.
	###################
	v = (n*R*T)/p # do something
	print("Volume result from function:", v, "liters") 
	return v # return the result of the function

#########################################################
# Use the function one time.
#########################################################
v = idealGasLaw(pressure, moles, gasConstant, temperature)

#########################################################
# Use the function mutliple times in a loop.
#########################################################

# Functions enable compact, portable, and reusable code.
########################################################
moles = range(1,11) # create a list of integers from 1 to 10
vList = []
for mole in moles:
	v = idealGasLaw(pressure, mole, gasConstant, temperature) # Function usage within loop.
	vList.append(v)
i = 0
while i < len(vList):
	print("Moles: ", moles[i], " Liters: ", vList[i])
	i += 1

##############################################################
# The next two points are critical to understanding functions. 
##############################################################

# Point 1) 
# Number objects are passed "by value", i.e. "a new local copy of the object is created in the function".
#########################################################################################################
def byValue(intArg):
	intArg += 1
	return intArg

a = 1
print("Initial value of variable 'a':", a)
print("Return value of byValue function:", byValue(a)) 
print("Did variable 'a' change?", a) # No, because only the new copy of "a" in the function was altered.
a = byValue(a)
print("Did variable 'a' change now?", a) # Yes, because "a" has been reassigned the return value of the function byValue.

# Point 2) 
# List and dictionary objects are passes "by reference", i.e. "the actual object (it's address in memory) is passed".
#####################################################################################################################
def listByReference(listArg):
	listArg.append(100)
	return listArg

aList = [1, 2, 3, 4]
print("Initial value of the list:", aList)
print("Return value of listByReference function:", listByReference(aList)) 
print("Did the list change?", aList) # Yes, because the memory address for the actual list is what was passed to the function.

# Dictonaries are also passed "by reference".
#############################################
def dictByReference(dictArg):
	dictArg[1] = "NO!"
	return dictArg

aDict = {0: "YES", 2: "WE", 3: "CAN"}
print("Initial value of the list:", aDict)
print("Return value of dictByReference function:", dictByReference(aDict)) 
print("Did the dictionary change?", aDict) # Yes, because the memory address for the actual dictionary is what was passed to the function.

# Writing functions with optional arguments or functions that have arguments with default values. 
#################################################################################################
def functionWithOneOptionalArgument(arg, optionalArg=0):
	if optionalArg:
		answer = arg + optionalArg
	else:
		answer = arg
	return answer

a = 1
value = functionWithOneOptionalArgument(a)
print("Without an optional argument, the answer is:", value)
a = 1
b = 1
value = functionWithOneOptionalArgument(a, optionalArg=b)
print("With an optional argument, the answer is:", value)

# A function that does not have a return statement, automatically returns the "None" object.
############################################################################################
def functionThatWithNoReturnValue(a, b):
	answer = a + b

a = 1
b = 1
print("Why I am I not getting the answer to a + b?", functionThatWithNoReturnValue(a, b))

# To fix the above function, you need to add a return statement.
################################################################
def functionThatWithNoReturnValue(a, b):
	answer = a + b
	return answer

a = 1
b = 1
print("Now I am getting the answer to a + b!", functionThatWithNoReturnValue(a, b))









