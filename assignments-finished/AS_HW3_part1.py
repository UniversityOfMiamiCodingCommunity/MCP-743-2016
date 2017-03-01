# Equation #1 calculates the real roots of a quadratic equation using the quadratic formula.
a = 1
b = 1
c = -4
x1 = (-b + (b**2 - 4*a*c)**0.5) / (2 * a)
x2 = (-b - (b**2 - 4*a*c)**0.5) / (2 * a)
print("The first root of the quadratic is ",x1)
print("The second root of the quadratic is ",x2)

# Equation #2 calculates the number of IEQ (islet equivalents) of a particular distribution of islets
dist = {}
dist[50] = 4
dist[150] = 7
dist[250] = 10
dist[350] = 16
dist[450] = 4
totalVolume = 4/3*3.14159 * (dist[50]*50**3 + dist[150]*150**3 + dist[250]*250**3 +
	dist[350]*350**3 + dist[450]*450**3) 
stdVol = 4/3*3.14159*(150**3)
numIEQ = int(totalVolume/stdVol)
print(numIEQ, " islet equivalents")