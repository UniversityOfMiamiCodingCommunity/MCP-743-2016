def translate (seq):
	Isoleucine = ['I', 'ATT', 'ATC', 'ATA']
	Leucine = ['L', 'CTT', 'CTC', 'CTA', 'CTG', 'TTA', 'TTG']
	Valine = ['V', 'GTT', 'GTC', 'GTA', 'GTG']
	Phenylalanine = ['F', 'TTT', 'TTC']
	Methionine = ['M', 'ATG']
	Cysteine = ['C', 'TGT', 'TGC']
	Alanine = ['A', 'GCT', 'GCC', 'GCA', 'GCG']
	Glycine = ['G', 'GGT', 'GGC', 'GGA', 'GGG']
	Proline = ['P', 'CCT', 'CCC', 'CCA', 'CCG']
	Threonine = ['T', 'ACT', 'ACC', 'ACA', 'ACG']
	Serine = ['S', 'TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC']
	Tyrosine = ['Y', 'TAT', 'TAC']
	Tryptophan = ['W', 'TGG']
	Glutamine = ['Q', 'CAA', 'CAG']
	Asparagine = ['N', 'AAT', 'AAC']
	Histidine = ['H', 'CAT', 'CAC']
	GlutamicAcid = ['E', 'GAA', 'GAG']
	AsparticAcid = ['D', 'GAT', 'GAC']
	Lysine = ['K', 'AAA', 'AAG']
	Arginine = ['R', 'CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG']
	StopCodons = ['*', 'TAA', 'TAG', 'TGA']
	translatedSequence = []
	i = 0
	while i < len(seq) - 2:
		iCodon = seq[i:i+3]
		if iCodon in Isoleucine:
			translatedSequence.append("I")
			i += 3
		if iCodon in Leucine:
			translatedSequence.append("L")	
			i += 3		
		if iCodon in Valine:
			translatedSequence.append("V")	
			i += 3		
		if iCodon in Phenylalanine:
			translatedSequence.append("F")
			i += 3
		if iCodon in Methionine:
			translatedSequence.append("M")
			i += 3
		if iCodon in Cysteine:
			translatedSequence.append("C")
			i += 3
		if iCodon in Alanine:
			translatedSequence.append("A")
			i += 3
		if iCodon in Glycine:
			translatedSequence.append("G")
			i += 3
		if iCodon in Proline:
			translatedSequence.append("P")
			i += 3
		if iCodon in Threonine:
			translatedSequence.append("T")
			i += 3
		if iCodon in Serine:
			translatedSequence.append("S")
			i += 3
		if iCodon in Tyrosine:
			translatedSequence.append("Y")
			i += 3
		if iCodon in Tryptophan:
			translatedSequence.append("W")
			i += 3
		if iCodon in Glutamine:
			translatedSequence.append("Q")
			i += 3
		if iCodon in Asparagine:
			translatedSequence.append("N")
			i += 3			
		if iCodon in Histidine:
			translatedSequence.append("H")
			i += 3
		if iCodon in GlutamicAcid:
			translatedSequence.append("E")
			i += 3
		if iCodon in AsparticAcid:
			translatedSequence.append("D")
			i += 3
		if iCodon in Lysine:
			translatedSequence.append("K")
			i += 3
		if iCodon in Arginine:
			translatedSequence.append("R")
			i += 3
		if iCodon in StopCodons:
			translatedSequence.append("*")
			break
	fileDone = "".join(translatedSequence)
	print(fileDone)
