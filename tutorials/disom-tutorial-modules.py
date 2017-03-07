# When you are stuck or need to explore something new start here:
# https://docs.python.org/3/tutorial/
# Also, Stackoverflow is a great resource: 
# http://stackoverflow.com
#################################################################

############################################################################################################
# Throughout these tutorials, you may have to add your own print statements to see the results of the code.
############################################################################################################

# Important Python code from Modules and Packages
# If you need help or need to explore something new regarding modules start here:
# Introduction: https://docs.python.org/3/tutorial/modules.html
# Standary library modules (Chapter 6 to 36): https://docs.python.org/3/library/
##################################################################################

# Example of importing methods (i.e. functions) from the "os" module.
#####################################################################

# Import the functions mkdir and listdir.
#########################################
from os import mkdir, listdir

# listdir(".") returns a list of files in the current directory.
################################################################
print("\n")
directoryContents = listdir(".")
for file in directoryContents:
	# Note: everything is a file, even directories.
	###############################################
	print("Found file in this directory:", file)

raise SystemExit

# listdir("..") returns a list of files in the parent directory of the current directory.
#########################################################################################
print("\n")
directoryContents = listdir("..")
for file in directoryContents:
	# Note: everything is a file, even directories.
	###############################################
	print("Found file in the parent directory of this directory:", file)

# listdir("./class3-pdbExcerpts") returns a list of files in the directory "class3-pdbExcerpts".
################################################################################################
print("\n")
directoryContents = listdir("./class3-pdbExcerpts")
for file in directoryContents:
	# Note: everything is a file, even directories.
	###############################################
	print("Found file in the parent directory of this class3-pdbExcerpts:", file)

# mkdir() makes a new directory on the file system.
###################################################
directoryName = "testDirectory"
# Makes directory in the current directory.
###########################################
mkdir(directoryName)
# Makes directory in the parent directory of the current directory.
###################################################################
mkdir("../" + directoryName)
