### Write function for numbers assignment:
##################################################

###The following function converts degrees Celsius to degrees Kelvin and Farenheit.
###################################################################################

def temp_convert(celsius):
	K = celsius + 273.15
	F = (celsius * (9/5)) + 32.0
	message = "These equations indicate that " + str(celsius) + " degrees Celsius is " + str(F) + " degrees Farenheit and " + str(K) + "degrees Kelvin"
	print message
	
###Use temperature function
###########################
	
temp_convert(25.0)
temp_convert(42.3)





