data=open('C:\\Users\\Nil Su\\Documents\\GitHub\\MCP-743\\assignments-finished\\dna.fa')
sequence={}
for line in data:
    if line.startswith(">"):
        name=line[1:].rstrip('\n')
        sequence[name]=''
    else:
        sequence[name]=sequence[name]+line.rstrip('\n') #Creates a Dictionary with key(header) and value(dna sequence)
dna=sequence[name]                                      #Extracts the value a.k.a the dna sequence 
dna=dna.upper()
print("The DNA sequence (length="+str(len(dna))+") is:", dna)
#Calculate GC Content
def gc_content(dna):
    c = dna.count("C")
    g = dna.count("G")
    gc_total = g+c
    gc_content = gc_total*100/len(dna)
    return round(gc_content,2)
#Find the reverse complement
def DnaReverseComplement(seq):
    for base in seq:
        if base not in 'ATCGatcg':
            print ("Error: NOT a DNA sequence")
            return None
    seq1 = 'ATCGTAGCatcgtagc'
    seq_dict = { seq1[i]:seq1[i+4] for i in range(16) if i < 4 or 8<=i<12 }
    return "".join([seq_dict[base] for base in reversed(seq)])
#Find the complement
def DnaComplement (seq):
    for base in seq:
        if base not in 'ATCGatcg':
            print ("Error: NOT a DNA sequence")
            return None
    seq=seq.upper()
    seq1=seq.replace("T","W")
    seq2=seq1.replace("A","T")
    seq3=seq2.replace("W","A")
    seq4=seq3.replace("G","X")
    seq5=seq4.replace("C","G")
    complement=seq5.replace("X","C")
    return complement 
#Translate the DNA sequence
def DnaTranslate(seq):
    table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'(STOP)', 'TAG':'(STOP)',
        'TGC':'C', 'TGT':'C', 'TGA':'(STOP)', 'TGG':'W',
        }
    protein = []
    end = len(seq) - (len(seq) %3) - 1
    for i in range(0,end,3):
        codon = seq[i:i+3]
        if codon in table:
            aminoacid = table[codon]
            protein.append(aminoacid)
        else:
            protein.append("N")
    return "".join(protein)
# Generates the six possible frames per one sequence
def frame_id(seq):
    frames = {'+1':[],'+2':[],'+3':[],'-1':[],'-2':[],'-3':[]}
    seq_rev = DnaReverseComplement(seq)
    for j in range(0,3):
        temp = ''.join([seq[j::]])
        temp_rev = ''.join([seq_rev[j::]])
        seq_trans = DnaTranslate(temp)
        seq_rev_trans = DnaTranslate(temp_rev)
        if j==0:
            frames['+1']=seq_trans
            frames['-1']=seq_rev_trans
        if j==1:
            frames['+2']=seq_trans
            frames['-2']=seq_rev_trans
        if j==2:
            frames['+3']=seq_trans
            frames['-3']=seq_rev_trans
            return frames
frame=str(frame_id(dna))
new_file = open("C:\\Users\\Nil Su\\Documents\\GitHub\\MCP-743\\assignments-finished\\output.txt", "w")
new_file.write("The DNA sequence (length="+str(len(dna))+") is:"+ dna+"\n\n")
new_file.write("The GC content (%) of the DNA sequence is: "+str(gc_content(dna))+"%"+"\n\n")
new_file.write("Reverse DNA Complement: "+DnaReverseComplement(dna)+"\n\n")
new_file.write("Dna Complement: "+DnaComplement(dna)+"\n\n")
new_file.write("The translated protein (Frame +1) is: "+DnaTranslate(dna)+"\n\n")
new_file.write("Six possible frames of translation: "+frame+"\n\n")
new_file.close()




