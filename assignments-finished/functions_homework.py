# For converting between relative centrifigul force (RCF) and rotations per minute (RPM)
########################################################################################

def centrifugeRCFeqn(r, rpm):
	RCF = (1.118 * 10**-5) * r * rpm**2
	print("Relative centrifugal force: ", RCF, "g's'")
	return RCF

centrifugeRCFeqn(14, 12000)

# For converting temperatures measured in fahrenheit to celcius or kelvin
#########################################################################

def tempFtoC(Tf):
	Tc = (Tf - 32) * 5 / 9
	print("Temperature: ", Tc, "\u00b0C")
	return Tc

tempFtoC(70)

def tempFtoK(Tf):
	Tc = (Tf - 32) * 5 / 9
	Tk = (Tc + 273.15)
	print("Temperature: ", Tk, "K")
	return Tk

tempFtoK(70)
