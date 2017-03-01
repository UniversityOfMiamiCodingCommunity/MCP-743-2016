#### INFO ####
# This script makes RFMix Input from Beagle phased files.
# USAGE: R CMD BATCH -chr ConvertToRFMixFormat.R
# LAST UPDATE: 2010-06-09 01:01:21
#############

## READS input options
rm(list=ls())
chr=commandArgs()[7]
chr=substr(chr, 2, nchar(chr))

admix = read.table(paste("/projects/scratch/ms/beecham/beagle_sept2016/Output/phased.ADMIX_CHR", chr, ".bgl.gz.phased.gz",sep=""), header=T, stringsAsFactors=F)
admix = admix[, -c(1:2)]
admixT = t(admix)
numadmix = nrow(admixT)

eur = read.table(paste("/projects/scratch/ms/beecham/beagle_sept2016/RFMIX_REF/Beagle_ID/EUR_CHR", chr, ".bgl.gz",sep=""), header=T, stringsAsFactors=F)
eur = eur[, -c(1:2)]
eurT = t(eur)
numeur = nrow(eurT)

afr = read.table(paste("/projects/scratch/ms/beecham/beagle_sept2016/RFMIX_REF/Beagle_ID/AFR_CHR", chr, ".bgl.gz",sep=""), header=T, stringsAsFactors=F)
afr = afr[, -c(1:2)]
afrT = t(afr)
numafr = nrow(afrT)

asia = read.table(paste("/projects/scratch/ms/beecham/beagle_sept2016/Output/phased.HGDP_CHR", chr, ".bgl.gz.phased.gz",sep=""), header=T, stringsAsFactors=F)
asia = asia[, -c(1:2)]
asiaT = t(asia)
numasia = nrow(asiaT)

all = rbind(admixT, eurT, afrT, asiaT)

binarize = function(snp){
	asFactor = factor(snp)
	allele1 = levels(asFactor)[1]
	allele2 = levels(asFactor)[2]
	result = rep(NA, length(snp))
	result[snp == allele1] = '0'
	result[snp == allele2] = '1'
	return(result)
}

all01 = apply(all, 2, binarize)

# Transpose back
alleles = t(all01)

write.table(alleles, paste("/projects/scratch/ms/beecham/rfmix_sept2016/alleles/alleles_CHR", chr, ".txt", sep=""), quote=F, sep="", col.names=F, row.names=F)

# Classes
classes = c(rep(0,numadmix), rep(1, numeur), rep(2, numafr), rep(3,numasia))
classesM = matrix(classes, nrow=1)
write.table(classesM, paste("/projects/scratch/ms/beecham/rfmix_sept2016/classes/classes_CHR", chr, ".txt", sep=""), quote=F, row.names=F, col.names=F)
