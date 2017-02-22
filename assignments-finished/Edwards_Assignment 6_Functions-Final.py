#Jasmine: equation 1: Newton's Law of Universal Gravitation F = G((m1 * m2)/r**2)

#G is gravatational constant, in N * ((m/kg)**2)

G = 6.674 * (10 ** -11)

print(G)

# Variables: m1 is mass of 1st object, while m2 is mass of second object- in kilograms

m1 = 20.0
m2 = 10.0

M = m1 * m2

print(M)

# Variable: r is the distance between two objects, in meters

r = 100.0 **2

print(r)

# Plug it in

F = G * (M/r)

print("Force; ", F, "Newtons")


def Gravitation(M, r, G): 
	F = G * (M/r) 
	print("Force result from function", F, "Newtons") 
	return F 

M = range(1,11) 
FList = []
for M in M:
	F = Gravitation(M, r, G) 
	FList.append(F)
 
 




#~ #Jasmine 2nd equation: Kinetic Energy KE = 1/2 M * V^2, in Joules 

#~ #M is mass of moving object, in kilograms (kg)

M = 50.0

#~ # V is velocity of object in meter per second (m/s)

v = 100.0

V = v**2

#plug and chug

KE = 0.5 * (M *V)

print("Kinetic Energy;", KE, "Joules")

def Energy(V, M): 
	KE = 0.5 * (M * V)
	print("Energy result from function:", KE, "Joules") 
	return KE

M = range(1,11) 
KEList = []
for M in M:
	KE = Energy(M, V)
	FList.append(F)
