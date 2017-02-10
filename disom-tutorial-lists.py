# When you are stuck or need to explore something new start here:
# https://docs.python.org/3/tutorial/
# Also, Stackoverflow is a great resource: 
# http://stackoverflow.com
#################################################################

############################################################################################################
# Throughout these tutorials, you may have to add your own print statements to see the results of the code.
############################################################################################################

# Lists and Tuples 
# If you need help or need to explore something new regarding list and tuples (sequences in general) start here:
# Overview: https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
# List Methods: https://docs.python.org/3/tutorial/datastructures.html
################################################################################################################

# The most boring example list ever. 
####################################
exampleList1 = [10, 3, 5, 1, 2, 5, 6, 9, 8, 7, 4]

# Get slice.
############

# Pop an element. 
#################
print("Pop example:", exampleList1)
poppedItem = exampleList1.pop(-1)
print("Pop example:", exampleList1)

# By far, the most common list method you will use is sort(), and maybe reverse().
##################################################################################
exampleList1.sort()
print("Sort example:", exampleList1)
exampleList1.reverse()
print("Sort example:", exampleList1)

# The second-most boring example list ever. 
###########################################
exampleList2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# One way to combine two lists into one:
#########################################
combinedList1 = exampleList1 + exampleList2
print("Combining lists example 1:", combinedList1)
# Why not sort it?
###################
combinedList1.sort()
print("Sorted combined lists example 1:", combinedList1)

# Another way to combine two lists: using the list method extend().
###################################################################
combinedList2 = []
combinedList2.extend(exampleList1)
combinedList2.extend(exampleList2)
print("Combining lists example 2:", combinedList2)
# Why not sort it?
###################
combinedList2.sort()
print("Sorted combined lists example 2:", combinedList2)

#####################################################################################################################
#
# OH MY GOD, I am so bored with list methods and concepts because they are so similar to string methods and concepts!
#
#####################################################################################################################

# Tuples are like lists, but they are immutable, and are denoted by parenthesis () instead of brackets []. They are equally as boring.
######################################################################################################################################

# I am so lazy that I am not even going to type out an example tuple.
# Instead I will convert our combinedList2 list to a tuple using the built-in Python type conversion function tuple().
######################################################################################################################
# TADA!
########
combinedTuple = tuple(combinedList2)

# All of the list operations and methods that do not involve mutation, are available for tuples.
# For example:
# Get value by index.
#####################
print ("Tuple index example:", combinedTuple[5])
# Get the length of the tuple.
##############################
print ("Tuple length example:", len(combinedTuple))
# Get a tuple slice.
####################
print ("Tuple slice example:", combinedTuple[2:5])

