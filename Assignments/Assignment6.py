# 1) 

# Hardy Weinberg Equation ##############################################

def hW(p,q):
	hWC = (p**2)+(2*p*q)+(q**2)
	print("Hardy Weinberg Coefficient: " + str(hWC))
	return hWC

p=0.7
q=0.2

hW(p,q)

# Population Growth Based on Generation Number #########################

def pG(n,q,g):
	c = (n)*(q**g)
	print("Population Growth: " + str(c))
	return c

n=4
q=6
g=2

pG(n,q,g)

########################################################################
# 2)

class Virus():
	def __init__ (self, name, tValue, naType):
		self.name = name
		self.tValue = tValue
		self.naType = naType
	def return_info(self):
		info = '\n' + self.name + ', ' + str(self.tValue) + ', ' + self.naType
		return info
		
########################################################################
# 3)

v1 = Virus('Herpes Simplex 1',16,'linear dsDNA')
v2 = Virus('Adenovirus',25,'linear dsDNA')
v3 = Virus('Human Papillomavirus',7,'circular dsDNA')
vList = [v1,v2,v3]
for v in vList:
	print(v.return_info())

########################################################################
# 4)

# PENDING
