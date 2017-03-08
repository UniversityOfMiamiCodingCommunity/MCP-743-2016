########################################################################
# Assignment
# Code two scientific equations of your choosing in Python.
# Make sure the equations are fully commented. See my example below.
########################################################################

#  1) Hardy Weinberg Equation ##########################################

# Variable representing probability of allele 1
p = 0.3
# Variable representing probability of allele 2
q = 0.5

# Equation determining if allelic distrubution is not in equillibrium with the expected ratio (that is, natural selection is taking place on these alleles)
HW = (p**2)+(2*p*q)+(q**2)

print("Considering that a value of 1 represents total equillibrium and lack of natural selection in this population, the Hardy Weinberg proportion for this set of alleles in said population is " + str(HW))

#  2) Population Growth Based on Generation Number #####################

# Variable representing number of generations
g = 3
# Variable representing size of initial population
n = 3548
# Variable representing average number of offspring per parent in each generation (assuming this does not vary by generation, which in real life it almost certainly would)
q = 2

# Equation for population growth based on generations (producing similar number of offspring)
c=(n)*(q**g)

print("\nBased on a population reproducing at a steady rate, the predicted population growth over the given number of generations is " + str(c))
