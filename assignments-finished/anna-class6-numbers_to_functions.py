####################
# Anna's equations #
####################

#######################
# Equation for velocity

vi = 5.0 # initial velocity in meters per second
a = 9.8 # acceleration of gravity in meters per second squared
t = 2.5 # time in seconds

vf = vi + a * t # solve for final velocity in meters per second
print("Final velocity: " + str(vf) + " m/s")

# convert equation to function
def velocity(vi, a, t):
	v = vi+(a*t)
	print("Final velocity from function:", v, "m/s")
	return v
v = velocity(vi, a, t)

#######################
# Equation for E = mc2

m = 0.4 # mass in kilograms
c = 3.00*10**8 # speed of light in meters per second

E = m * c**2 # solve for energy in Joules
print("Energy: " + str(E) + " Joules")

# convert equation to function
def energy(m, c):
	E = m*(c**2)
	print("Energy from function:", E, "Joules")
	return E
E = energy(m, c)