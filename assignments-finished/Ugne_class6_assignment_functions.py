########################################################################
# Example 1: momentum
########################################################################
# p = mv

#variable for mass (in kg)
mass = 50

#variable for velocity (in m/s)
velocity = 50

#variable for momentum (p)////solve for p
p = mass*velocity

#print("The momentum is ", p , "kg*m/s")



def momentum(m, v):
	p = m * v
	print("Momentum result: ", p, "kg*m/s", " Mass: ", m, "kg")
	return p

##Use function one time
p = momentum(mass, velocity)

#Use function in a loop
masses = range(1,11)
for mass in masses:
	p = momentum(mass, velocity)
	#print("Mass: ", mass, " Momentum: ", p)




###################################################################################
#Example 2: force of gravity acting on two bodies
####################################################################################
# F = (G*m_1*m_2)/(r**2)

#Gravitational constant in (N * m**2)/(Kg**2)
Grav_const = 6.67e-11

#mass of object_1 (in Kg)
mass_1 = 100

#mass of object_2 (in Kg)
mass_2 = 10

#radius (in cm)
radius = 50

#variable Force
F = (Grav_const * mass_1 * mass_2)/(radius**2)

#use function once
#print("The Force due to gravity is ", F, "N")


def forceOfGravity(G, m_1, m_2, r):
	F = (G * m_1 * m_2)/(r**2)
	print("Gravitational force result: ", F, "N", " for mass_1= ", mass)
	return F

F = forceOfGravity(Grav_const, mass_1, mass_2, radius)

####use function in a loop
masses = range(1,10)
for mass in masses:
	F = forceOfGravity(Grav_const, mass, mass_2, radius)
	#print("Mass_1: ", mass, "kg", "Mass_2: ", mass_2,"kg", " Force of Gravity: ", F)
