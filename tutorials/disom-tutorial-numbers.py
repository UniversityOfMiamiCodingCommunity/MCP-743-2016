# Date: 2017.01.28
###################

# When you are stuck or need to explore something new start here:
# https://docs.python.org/3/tutorial/
# Also, Stackoverflow is a great resource: 
# http://stackoverflow.com
#################################################################

############################################################################################################
# Throughout these tutorials, you may have to add your own print statements to see the results of the code.
############################################################################################################

#################################################################################
# Numbers
# If you need help or need to explore something new regarding numbers start here:
# https://docs.python.org/3/tutorial/introduction.html#numbers
#################################################################################

# In Python a variable is assigned using the "=" sign (e.g. a = 1 below).
# There are two primary number types in Python:
#########################################################################

# 1) Integers: all whole numbers (i.e. no decimal points)
##########################################################################
a = 1
b = 2

# The usual mathematical operations are available for integers. 
###############################################################
answer1 = a + b
answer2 = a - b
answer3 = a * b
answer4 = a / b

# You don't need to have spaces bewteen operators and numbers, but spaces help with readability. 
# For example, these expressions give equivalent answers to those above. 
################################################################################################
answer1 = a+b
answer2 = a-b
answer3 = a*b
answer4 = a/b

# 2) Floats: floating point numbers (i.e. numbers with decimal values)
######################################################################
a = 1.0
b = 2.0

# The usual mathematical operations are available for floats. 
#############################################################
answer1 = a + b
answer2 = a - b
answer3 = a * b
answer4 = a / b

# There is an operator for floats that you may not be familiar with called the modulo (%).
# It returns the remainder of a division operation.
###########################################################################################
answer5 = a % b # remainder is 1.0
b = 1.0
answer6 = a % b # now that we reassigned the variable b, the remainder is 0

#############################################################
# There are other, infrequently used operators for floats.
# For a full list explore the links at the top of this page. 
#############################################################