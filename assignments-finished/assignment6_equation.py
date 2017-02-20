{
    "cmd": ["/usr/local/bin/python3", "-u", "$file"],
}
#Energy Calculator
##################

#input mass
mass = 50

#speed of light constant
lightConstant = 2.99792458e+8

#Energy Equation
Energy = mass * (lightConstant**2)
print("Energy is " , Energy)


def EnergyCalc(m,c):
    E = m * (c**2)
    print('Energy from function is' , E)
    return E
