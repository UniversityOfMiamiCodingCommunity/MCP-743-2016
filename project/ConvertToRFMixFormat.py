import numpy as np
import pandas as pd

## READ INPUT FILES ##

admix = open("phased.ADMIX_CHR22.bgl.gz.phased", "r")
eur = open("EUR_CHR22.bgl", "r")
afr = open("AFR_CHR22.bgl", "r")
nam = open("phased.HGDP_CHR22.bgl.gz.phased", "r")

## Create function to create matrix from data

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

## Use matrix function on each data set

admixMatrix = createMatrix(admix)
eurMatrix = createMatrix(eur)
afrMatrix = createMatrix(afr)
namMatrix = createMatrix(nam)

for a in afrMatrix:
	print a

## Convert each matrix to a data frame

admixDataFrame = pd.DataFrame(admixMatrix)
eurDataFrame = pd.DataFrame(eurMatrix)
afrDataFrame = pd.DataFrame(afrMatrix)
namDataFrame = pd.DataFrame(namMatrix)

## Compute length of each data frame

admixNum = len(admixDataFrame)
eurNum = len(eurDataFrame)
afrNum = len(afrDataFrame)
namNum = len(namDataFrame)

## Create function to binarize data frames

def binarize(snp): # define function

	result = pd.factorize(snp)[0]
	return result

## Row bind data frames

#allDataFrame = pd.concat(admixDataFrame,eurDataFrame,afrDataFrame,namDataFrame)

#all01 = dataframe.apply(binarize,axis=0)

#for a in all01:
	#print all01

	


