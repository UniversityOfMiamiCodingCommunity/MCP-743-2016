import numpy as np
import pandas as pd

## READ INPUT FILES ##

admix = open("phased.ADMIX_CHR22.bgl.gz.phased", "r")
eur = open("EUR_CHR22.bgl", "r")
afr = open("AFR_CHR22.bgl", "r")
nam = open("phased.HGDP_CHR22.bgl.gz.phased", "r")

## MAKE FUNCTION TO CREATE MATRIX FROM INPUT FILES ##

def createMatrix(data):
	matrix = []
	n = 0
	
	for line in data:
		splitLine = line.split()
		newline = splitLine[2:]
		if not matrix:
			for sampleID in newline:
				matrix.append([sampleID])
		else:
			i = 0
			while i < len(newline):
				matrix[i].append(newline[i])
				i += 1
		n += 1
		#if n > 5:
			#break
	return matrix

## USE MATRIX FUNCTION ON EACH INPUT FILE ##

admixMatrix = createMatrix(admix)
eurMatrix = createMatrix(eur)
afrMatrix = createMatrix(afr)
namMatrix = createMatrix(nam)

#for a in eurMatrix:
	#print a

## CONVERT EACH MATRIX TO A DATA FRAME ##

admixDataFrame = pd.DataFrame(admixMatrix)
eurDataFrame = pd.DataFrame(eurMatrix)
afrDataFrame = pd.DataFrame(afrMatrix)
namDataFrame = pd.DataFrame(namMatrix)

#print admixDataFrame

## COMPUTE LENGTH OF EACH DATA FRAME ##

admixNum = len(admixDataFrame)
#print admixNum
eurNum = len(eurDataFrame)
#print eurNum
afrNum = len(afrDataFrame)
#print afrNum
namNum = len(namDataFrame)
#print namNum

## ROW BIND ALL DATA FRAMES ##

frames = [admixDataFrame,eurDataFrame,afrDataFrame,namDataFrame]
allDataFrame = pd.concat(frames)

#print allDataFrame

## CREATE FUNCTION TO BINARIZE DATA FRAMES ##

def binarize(snp): # define function

	result = pd.factorize(snp)[0]
	return result

## BINARIZE THE COMBINED DATA FRAME ##

all01 = allDataFrame.apply(binarize,axis=0)

#print all01

## WRITE 'ALLELES' FILE FOR RFMIX INPUT ##

all01.to_csv("ALLELES.txt",sep=' ',header=False,index=False)

## WRITE 'CLASSES' FILE FOR RFMIX INPUT ##

admixClass = [0]*admixNum
eurClass = [1]*eurNum
afrClass = [2]*afrNum
namClass = [3]*namNum

allClass = admixClass + eurClass + afrClass + namClass

thefile = open('CLASSES.txt','w')
for item in allClass:
	thefile.write("%s\n" % item)
	
	


