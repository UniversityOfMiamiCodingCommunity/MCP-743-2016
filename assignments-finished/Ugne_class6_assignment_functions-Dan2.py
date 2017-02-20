# Example: momentum
# p = mv

#variable for mass (in kg)
mass = 50

#variable for velocity (in m/s)
velocity = 50

#variable for momentum (p)////solve for p
p = mass*velocity

print("The momentum is ", p , "kg*m/s")



def momentum(m, v):
	p = m * v
	print("Momentum result: ", p, "kg*m/s")
	return p

##Use function one time
#p = momentum(mass, velocity)

##Use function in a loop
masses = range(1,10)
pList = []
for mass in masses:
	p = momentum(mass, velocity)
	pList.append(p)

	# i = 0
	# while i < len(pList):
	# 	print("Mass: ", mass[i], " Momentum: ", pList[i])
	# 	i +=1









#Example: force of gravity acting on two bodies
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

print("The Force due to gravity is ", F, "N")


# def forceOfGravity(G, m_1, m_2, r):
# 	F = (Grav_const * mass_1 * mass_2)/(radius**2)
# 	print("Gravitational force result: ", F, "N")
# 	return F

# Dan's fix.
def forceOfGravity(G, m_1, m_2, r):
	# Make sure you use the arguments names inside the function.
	F = (G * m_1 * m_2)/(r**2)
	print("Gravitational force result: ", F, "N")
	return F

###use function once
F = forceOfGravity(Grav_const, mass_1, mass_2, radius)

####use function in a loop
mass_1 = range(1,10)
# F_list = []
for mass in mass_1:

	# F = forceOfGravity(Grav_const, mass_1, mass_2, radius)
	# Dans fix 
	F = forceOfGravity(Grav_const, mass, mass_2, radius)

	print("Mass_1:", mass, " Force of Gravity: ", F)

	# F_list.append(F)

	# i = 0
	# while i < len(F_list):
	# 	#print("Mass_1:", mass[i], " Force of Gravity: ", F_list[i])

	# 	# Dan's fix
	# 	print("Mass_1:", mass, " Force of Gravity: ", F_list[i])

	# 	# Don't forget to add i!
	# 	i += 1

