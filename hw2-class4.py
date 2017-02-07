# 1) 
# Open the subsequence of chromosome 17 containing the gene for p53, and parse the DNA sequence into a single string.
# This sequence is in the file named sequence-p53.fasta in the dataFiles directory.
#####################################################################################################################


# 2)
# Find all possible start codons in parsed DNA sequence.
# Write your results to file named startCodonIndices.txt.
# The file should be formatted such that:
# a) the first line reports the total number of startCodons
# b) the additional lines report a single start codon index
#################################################################################################

# 3)
# Find all possible stop codons in parsed DNA sequence.
# Write your results to file named stopCodonIndices.txt.
# The file should be formatted such that:
# a) the first line reports the total number of stopCodons
# b) the additional lines report a single stop codon index 
#################################################################################################


>NG_017013.2:5001-24149 Homo sapiens tumor protein p53 (TP53), RefSeqGene (LRG_321) on chromosome 17
p53sequence = "GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTC
TAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTG
CTTTCCACGACGGTGACACGCTTCCCTGGATTGGGTAAGCTCCTGACTGAACTTGATGAGTCCTCTCTGA
GTCACGGGCTCTCGGCTCCGTGTATTTTCAGCTCGGGAAAATCGCTGGGGCTGGGGGTGGGGCAGTGGGG
ACTTAGCGAGTTTGGGGGTGAGTGGGATGGAAGCTTGGCTAGAGGGATCATCATAGGAGTTGCATTGTTG
GGAGACCTGGGTGTAGATGATGGGGATGTTAGGACCATCCGAACTCAAAGTTGAACGCCTAGGCAGAGGA
GTGGAGCTTTGGGGAACCTTGAGCCGGCCTAAAGCGTACTTCTTTGCACATCCACCCGGTGCTGGGCGTA
GGGAATCCCTGAAATAAAAGATGCACAAAGCATTGAGGTCTGAGACTTTTGGATCTCGAAACATTGAGAA
CTCATAGCTGTATATTTTAGAGCCCATGGCATCCTAGTGAAAACTGGGGCTCCATTCCGAAATGATCATT
TGGGGGTGATCCGGGGAGCCCAAGCTGCTAAGGTCCCACAACTTCCGGACCTTTGTCCTTCCTGGAGCGA
TCTTTCCAGGCAGCCCCCGGCTCCGCTAGATGGAGAAAATCCAATTGAAGGCTGTCAGTCGTGGAAGTGA
GAAGTGCTAAACCAGGGGTTTGCCCGCCAGGCCGAGGAGGACCGTCGCAATCTGAGAGGCCCGGCAGCCC
TGTTATTGTTTGGCTCCACATTTACATTTCTGCCTCTTGCAGCAGCATTTCCGGTTTCTTTTTGCCGGAG
CAGCTCACTATTCACCCGATGAGAGGGGAGGAGAGAGAGAGAAAATGTCCTTTAGGCCGGTTCCTCTTAC
TTGGCAGAGGGAGGCTGCTATTCTCCGCCTGCATTTCTTTTTCTGGATTACTTAGTTATGGCCTTTGCAA
AGGCAGGGGTATTTGTTTTGATGCAAACCTCAATCCCTCCCCTTCTTTGAATGGTGTGCCCCACCCCGCG
GGTCGCCTGCAACCTAGGCGGACGCTACCATGGCGTGAGACAGGGAGGGAAAGAAGTGTGCAGAAGGCAA
GCCCGGAGGTATTTTCAAGAATGAGTATATCTCATCTTCCCGGAGGAAAAAAAAAAAGAATGGGTACGTC
TGAGAATCAAATTTTGAAAGAGTGCAATGATGGGTCGTTTGATAATTTGTCGGAAAAACAATCTACCTGT
TATCTAGCTTTGGGCTAGGCCATTCCAGTTCCAGACGCAGGCTGAACGTCGTGAAGCGGAAGGGGCGGGC
CCGCAGGCGTCCGTGTGGTCCTCCGTGCAGCCCTCCGGCCCGAGCCGGTTCTTCCTGGTAGGAGGCGGAA
CTCGAATTCATTTCTCCCGCTGCCCCATCTCTTAGCTCGCGGTTGTTTCATTCCGCAGTTTCTTCCCATG
CACCTGCCGCGTACCGGCCACTTTGTGCCGTACTTACGTCATCTTTTTCCTAAATCGAGGTGGCATTTAC
ACACAGCGCCAGTGCACACAGCAAGTGCACAGGAAGATGAGTTTTGGCCCCTAACCGCTCCGTGATGCCT
ACCAAGTCACAGACCCTTTTCATCGTCCCAGAAACGTTTCATCACGTCTCTTCCCAGTCGATTCCCGACC
CCACCTTTATTTTGATCTCCATAACCATTTTGCCTGTTGGAGAACTTCATATAGAATGGAATCAGGCTGG
GCGCTGTGGCTCACGCCTGCACTTTGGGAGGCCGAGGCGGGCGGATTACTTGAGGATAGGAGTTCCAGAC
CAGCGTGGCCAACGTGGTGAATCCCCGTCTCTACTAAAAAATACAAAAATTAGCTGGGCGTGGTGGGTGC
CTGTAATCCCAGCTATTCGGGAGGGTGAGGCAGGAGAATCGCTTGAACCCGGGAGGCAGAGGTTGCAGTG
AGCCAAGATCGTGCCACTACACTCCAGCCTGGGCGACAAGAACGAAACTCCGTCTCAAAAAAAAGGGGGG
AATCATACATTATGTGCTCATTTTTGTCGGGCTTCTGTCCTTCAATGTACTGTCTGACATTCGTTCATGT
TGTATATATCAGTATTTTGCTCCTTTTCATTTAGTATAGTCCATCGATTGTATATCCGTCCTTTTGATGG
CCTTTTGAGTTGTTTCCCATTTGCGGTTATGAAATAAAGCTGCTATAAACATTCTTGTACAATTCTTTTT
GTGATCATATGTTTTCGTGTTTCTTGGAGAAATACTTAGGAGGGGAATTGCGAGTTTGGAAGTAAAAAGT
AGCTGTATTTTGAACTTTTTCAGAAGCTCTGAGTTTTCCAGAGCGGTTGTACCATTTTACACTCCAACTA
GCAAGGTATGGGAGTTATTATGGTTGTGCCACAGCCTTCCGGACATTAGGTATTGTCAGTCTTTCTAATG
TGGTATATCCTTGTGGTTGTAATTTACAGTTCTCTATTGACTAAGGATGTTCAGCATTTTTTCATGTGCC
TATTGGCCATTCGTATTTTGTTTGTAAAGTAGCTCTTCGAGTCTTTTACCTGTTATTTTGGTTTTTTGTT
TGTTTTTATTGTTCAGTTGTGGGACTGCTTTATACATTCTGGATACAAGTCCTTTATCAGATCCATGTGT
CGTGAATGTTTTCTTCTGATCTGTTGCTTGCCTATTTGTTTGCTTTACAGAGTTTACAGTATCTTAAGAG
GAGTGGATTTATCTTTTTTATGTTCAGTATTTGCCTTGTCCTGTTTAGGACATCTTTTTTTTTTTTTTTA
ACCCCAGGGTCATGAAGATATTATCTTACATTTTCTTTTAGGACCTTTATGGTTGTAAGTTTTACAGTAA
GGTCCTTGAGCCATTAATTAATTCTTAAAATTAATTGTTTATGGTGTGAGGTGTAGGAGTCAGTCTCTGG
TATCTTTCCTGTATGGAAATCCAGTTATTCTGTCTCCACTTGTTGAAATAGGCTTCCTTTCTCTACTGAA
TGCTTTTAATTTTAATTATTTTACAGTTGGAGTATAGGGCTACCATTTTAGTGCTATTTTCTTTTTTTCT
TTGTTAATTTTTGAGACAGGGACTCACACTGTTGCCCAGGCTAGAGTACAATGGCACAATCAAGGCTTAC
TGCAGCCTCGAACCCCTGGGCTCAAGCAGTCCTCTAGCAGCCTCACGAGTAGCTGGGATTACTCCACCAC
ACCCAGCTAACTATTTTATTTTTTTGTATTGACAGGATCTCACTATGTTGCCCAGGCTGGTCTCAAACTG
CTGGCCTCAAGCTTTCATCCCATCTCGGCCTCCCAAAGTGCTGGGATTACAGGTGTGAGCCACCATGCCT
GACCTCTTAGTGCTATTTTCTATTTATCTCCTCTGTTCTCTGCTCTCTTTAAACGTTGGAGGAAGAAACA
GTACCCATCTTACACAAACTCTTCAGAAAACAGAGGAACAGACTGGGCGCGGTGGCTCATACCTGTAATC
TCAGCACTTTGGTACGCTGAGGCAGGGGATCATTTGAGGTCGGGAGTTCGAGACCAGCCTGGCCAACACG
GCGAAACCCCATCTCTACTAAAAATACAAAAAGTAGCTAGGCGTGGTGACACATACCTGTAATGCCAGTT
ACTCAGGAGGCTGAGGCACAAGAATCCCTTGAACCTGGGAAGCGGAGGTTGCAGTGAGCCGAGATTGCGC
CACTGCACTCCAGCCTGGGCAACAGAGTGAGACCCTGTCTCAGAAAAAAAAAGAAAGAAAGAAAAAATAG
AGGAATATTTCCCAACTTGTTTTCGAAGCCAGCATAATCCTGGTACCAAAACCAAACAAGGACATTATAA
GAAAAGAAAATATAGACCAATATTCCTGTTAGCATAGACATGCAACAGCTAACCAATTTTAGCAAACCAA
ACCTGGTAATATAGAAAAAAGGATAAATAGGCCAGTCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTG
GGAGGCTGAGGCAGGCAGATCACTTGAGGTCAGGAGTTTGAGACCAGCCTGACCAACATGGTGAAACCCC
GTTTCTAATAAAAATACAAAAATCAGGCTGGGCACGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAG
GCCGAGGTGGGCAGATCACGAGGTCAGGAGTTCAAGACCAGCCTGACCAATGTGGTGAAACGCCATCTCT
ACTAAAAATACAAAAATCAGCCGGTGTGGTGGCACCTGCCTGTAATCCCAGCTACTCAGGAGGCTGAGGC
AGAATTGCTTGAACCCGGGAGGCAGAGGTTGCAGTGAGCCAAGATCGTGCCACTGCACTCCAGCCTGGGC
GACAGAGCAAGACTTCATCTCAAAAAAAAAAAAAAATTAGCTGGGCATGGTGGTGGGCACCTGAAATCCC
AGCTACTCGGGAGTCTGAGGCAGGAGAATCGCTTGAACCCAGGAGGCAGAAGTTGCACTGAGCTGGGATC
ACACCATTGCACTCCAGCCTGGGCAACAGAGTGAGACTCCATCTCAAAAAAAGAAAAAGAAAAAGGATAA
ATACATTCTAACCAAATAATGTTTATCTCATGATTGTAGCTGATTCAACATTCAAAAATTGGCCTGGTGC
AGTAGCTCAGGCCTGTAATCCCAACATTTTAGGAGGCTGAGGCAGGAAGATCTCTTGAGCCCAGGATTTC
AAGACCAGCCTGGGCAACATAGTCAGACTGGTCTTTACTGGGGGGAAAAAAATCAGTCTGTGTAATTCAC
CACATTAACAAAGGGAAACATAAAAACCCTATGATCATTTCAACAGATGTAGCAAAAGCAGTTAATGATA
TTCAACACATATGCATGATTACAAACCAACCAACCTCCTAGCAAACTAGGGAAAGGAAACTTAACCTAGT
TTGATAACAGGGCGTCCACAGTCGGAGTTCCACTAGCAGCATACATAATGGTAGAAAACTCAGTGCTGCC
GGGCGCGGTGGCTCACGCCTGTAATGCCAGCACTTTGGGAGGCCTAGGCGGGCGGATCACGAGGTCAGGA
GATCGAGACTGTCCTGACTAGCATGCTGAAACCCCGTCTCTACTAAAAATACAAAAACAAAAAATTAGCC
GGGCATGGTGGCGGGCGCCTATAGTCCCAGCTACTCGGGAGGCTGAGGCGAGAGAATGGCGTGAACCCGG
GAGGCGGAGCTTGCAGAGCCTAGATCGTGCCACTGCACTCCAGCCTGGGTGACAGAGTGAGACTTCGTCT
CAAAAAAAAAAAAAAAAAAAAAAGAAAAGAAAACTCAACGCTTTTTCCTCTAAGATCAGGAACTAGAAAA
GGATTTGACTCTCACAACGTTGATACCATACTGGAGGTTTTAACCAGGCAAGAAAAAGAAATAATGAGGG
CCGGGTGCGGTGGCTCAGGCCTGTAATCCCAGCACTTTGGGAAGCCGAGACGGGTGGATCACGAGGTCAG
GAGATCGAGACCATCCTGGCTAACACGGTGAAACCCTGTCTCTACTAAATATACAAAAAATTAGCCGGGC
GTAGTGGCGGGCGCCTGTAGTCCCAGCTACTCGGGAGGCTGAGGCAGGAGAATGGCGTGAACTCAGGGGG
CGGAGCTTGCAGTGAGCTGAGATCGAGCCACTGCACTCCAGCCTGGGCGACAGAGCAAGACTGTGTCTCA
AAAAAAAAAAAAGAAAAAGAAATAATGATTAGTGGCCCGATGTCTCACGCCTATAATCCCAGCACTTTGG
GAGGCCGAGGTGGGCAGATCACCTGAGGTCTGGAGTTGGAGACCAGCCTGACAAAGATGGTGAAACCTCG
TCTCTATTAAAATATTAAAAAAATAGCCAGGCGTTGGCCGGGTACAGTGGCTCATGCCTGTAATCCCAGC
ACTTTGGGAGGCCGAGGTGGGTGGATCACCTGAGGTCAGGAGTTCAACACCAGCCTGGCCAACATGGTGA
AACCCCATCTCTACTAAAAATACAAAAATTAGCCGGGCGTAGTGGCGGGCGCCTGTAATCCCAGCTACTT
GGGAGGCTTAGGCAGGAGAATCGCTTGAACCTGGGAGGCGGAGGTTGTAGTGAGCCGAGATTGCACCATT
GCACTCCAGCCTGGGTGACAAAAGCAAAAACTCCGTCTCAAAAAAAAAAGAATTAGCCAGGGGTAGTGGT
GAACGCCTGTAGTCCCAGCTACTCAGGAGGCAGAGGCAGGAGAATCACTTGAACCCAGGAGGCAGAGGTT
GCAGTGAGCCGAGATTGTCCCATTGCACTCCAGCCTAGGCGACAAGAGCAAAATTCCATGTCAAAAAAAA
AAAAAAAAAAGGAAAGAAAAAAAATAACGATTAGAAAGGAAGAAATAAAACACATTCACAGCCAGTATGA
TTCTATACATACATGTCCTAATGGGGCCAGGCGTGGTGGCTCATGCCTGTAATCCTAGCACTTTTAGGAG
GCTGAGGCAGGTGGCTTCCCTGGGACCAGCCTGGCCAACATGGTGAAACCCCAACTCTAATAAAAATACA
AAAAATCAGCCAGGCGTGGTGACGGGCACCTCTAATCCCAGCTACTCAGGAGGCTGAGGCAGGAGAATTG
CTTGGACCTGGGAGGCAGAGGTTGCAGTGAGCCGAGATCGCGCTATTGCACTCCAGCCTGGGCAACAAGA
GTGAAACTCCGGCAGGGTGTGGTGGCTTACGCCTGTAATCCCAGCACTTCGGGAGGCTGAGGCAGGCCGA
TCACCTGAGGTCAGGAGTTTGAGACCAACCTAACATGGTGAAACCCCGTCTCTACTAAAAATACAAGAAT
TAGCTGGGTGTAGTGGTGGGCGCCTGTAATCCCAGCTACTTGGGAGGCTGAGACAGAAGAATTGCTTGAA
CCCAGGAGGTGGAGGTTGCAGTGAGCTGAGATCATGCCATTGCACACCACGCCGGGCAACAGAGCGAGAT
TCCGTCTCAAAAAAAAAAAAAAAGAGTGAAACTCTATCTCAAAAAAAAAAAAAAGTCCTAATGGAAAATC
CATAAAAAGCTACCAAAACTAATAAATAAATATAGCAGGGTTGCAGGTTACAGGGCAATATAGTTATCCC
TCTATCTGTAGGGGCTTGGTTCTGGGACTCCTCACACACCAAACCCACAGATGTCTAAGTCCCATATATA
AGACGGTATAGTATTTGGATTTAACCTACACATATCCTCCCATATAGTTTAAATTATCTCTAGATTACTT
ACATTACCCCCATACAATGAAAATGCTAATGTACATGCAAGTATGTATGTAAGTACTTGTACTATATTGT
TTAGGGAATCACTGGACATATAGGCCTTCAAGACTGATACCAGCAGCCACTGTTAAGATTCTGGTCAGGC
CTGCCCCTGTTTGGGGTCTCAGTTGATCTCATTGCCTTCCCACCCAGCCAAGGGCACCTGCATTTCTCTT
GGCTCCCTGGCCATTTGGAAGGCCTAGTTCAGCCTGGCACATTTGTATCCTGGCCCACTGATGCTGGTAC
CCCTGGGAAGGTCCTGCTCTGAAAAACACGGAGATTTTAGTTGCTACTGAAGATTTGAGAGATAAAGACA
GGGAGACCTGTCTGTAGACCTGTGTCCCTCCAAGTGGGATTGAGACTTTGGGCCCCCCATTTCAGGACAG
CACCTCCTGGCCTGTTGACTGAATAGATCCCTGAAGGAGGTGTACTTGCATTAATGGAGTGGGGGTGGGA
GCAGTACCACAGATCCGCACTAACAATCACACAGTTCTCTCTAGAATAATAATATAGAACAAGTGAAATA
GAACAATTGCAGAAAGAGCTAACCTTTGTTGAGCTCTTACTGTGTGCCCAGCACTTTCCTCAACTCTACA
TTTCCCATAATACACAGAGTACTAGGTAGGCCAGGCTTGGTGGCTCACGCCTGTAATCCCAGCACTTTAG
GAGGCCAAGGGGGGTGGATCACCTGAGGTCGGGAGTTCAAGACCAGCCTGACCAACATGGTGAAACCCCG
TCTCTACTAGAAGTACAAAATTAGCCAGGTGTGGTGGCACATGCTTGTAGTCCTAGCTACTCAGCAGGCT
GAGGCAGGAGAATCATTTGAATCCGGGAGGAGGTTGCAGTAAGCGGAGATAGTGCCACTGTACTCCAGCC
TGGGCAATAAGAGCTGAGACTCCGTCTCAAAATAAAATAAAATAAAATAAAATAAAATAAAATAAAATAA
AAAAAGAAAAGAGCCTGCCATTAAAGGAGCTGTTTGGTAGGGGATGTTTTGTCAGTGCAAACAACAGAAA
AGTGGGCTGGGCACAGTGGTTCATGCCTGTAATCCCAGCACTTTGGGAGGCCAAGGCGGGCGGATCACCT
GAAGTTGGGAGTTCAAGACCAGCCTGACCAATATGGAGAAACCCCGTCTCTACTAAAAATACAAAATTAG
CCGGGCGCAGTGGCGCATGCCTGTAATCCCAGCTACTCGGGAGGCTGAGGCAGGAGAATCGCTTGAACCT
GGGAGGCAGAGGTTGCGGTGAGCCGAGATCGCACCATTGCACTCCAGCCTGGACGAGAGCAAAACTCTGT
CTCAAAAAAAAAAAAAAACAGAAAAGTGTAACAAACACTTACAGTAGGCATGTTTCTTAGCAAATCTGAT
GACAAATTTGGCATAAAGAAAGAGAGCATCCCTGAAAAAAAAAAAAAGAAAAAGAAAGAGAGCATCCTGC
CTGGGCAACATAGTGAAACCCTGCCTCTACAAAAAAACTCAAAAATTGGCCGGGTGCAGTGGCTCACACC
TGTAATCCCAGCACTTTGGGAGTCGGAGGCGGGAGGATCACCTGAGGTCAGGAGTTCGAAACCAGCCTGG
CCAACATGGCAAAACCCCATCTCTACTAAAAATACAAAAAATTAATCAGGCGCATTGGTGGGCGCCTGTA
ATCCCAGCTACTCAGGAAGTTGAGGCAAGAGGATCGCTTGAATCTGGGAGGTGGAGGTTACAGTGAGTCG
AGATCACACCACTGCACTCTAGCCTGGGTGACAGGGCGAGACTCCGTCTCCAAAAAAAAAAAGAAAAAGA
AAAAGACTAAAAAATTAGCCAGGCAGGCCTCTGTGGTCCCAGCTACTTGGGAGGCTGAGGCAGGAGAATC
ACTGAGCCCAGGAGTCCGAGGCTGTAGTGAGCCATGATTGCACCACTGTACCCTAGCTTGGGCAACAAAG
CAAGACCCTGCCTCAAAAGAAAAAAGAAAGAAAGAAAGAACATGGCGGGCCAGGCACAGTGGCTCACACC
TGTAATCCCAGCGCTTTGAGAGGCCGAGGCAGGTGGATCACAAGGTCAGGAGTTCCACACCAGCCTGGCC
AACATGGTGAAACCCTGTCTCTACTAAAAATACAAAAAATCAGCCAGGCATGGTGGCAGGGGCCTGTAAT
CCCAGCTACTCGGGAGGCTGAGGCAGGAGAATTGCTTGAAACCAGAAGGCAGAGGTTGCAGTGAGCCTAG
ACTGCACCACTGCACTCCAGCCTGGGCGAAAAGAGCCAAACTCCATCTCAAAAAACAAACAAAAAAACAA
AACAAAAGAAAACATGGCAAAGCCTTTGAAAGCTTGTCTGGGAGAAGGTGCGATGATAGTTGCATAACTT
CGTGCAAGATGCTGGTCCACACAGGGGCTGCCCCTTGCTCTTTCTCGCTCTCTTAACCTCTCATATAACA
GGCTTGTGTGTTATTCACATTTATTGAGCCCAAGCAGGTGCAAGGCATTGTGATCTAATACTTTGGTCAG
CAAGACAACAAGATAGATCACTGCCCTGCCCTTAGGAAGTGTATATGCTATTAGAGGAAACAGATAAAAT
AAACAAGGAAAAGTATCAGACAATGTAAGTGCTATGAGAATGCAAATGAGGTGATGTGAATTAAAATAGG
ATGACTTAAAGTCTGCACGGGAAGGAGCCTACCCCCATGTTCCTGGCTAGCCAAGGAACCACCAGTTGAT
TAGCAGAGAAGGGCAGCCAGTCTAGCTAGAGCTTTTGGGGAAGAGGGAGTGGTTGTTAAGAGATGAGATT
AAAGAAGCCGAGACGGGCCATTCGTGAGGGGTTTGTAATGCAGGGCTGAGGAGTGTCCGAAGAGAATGGG
CAGGTGAGCGGTGAGACAGTTGTTCTTCCAGAAGCTTTGCAGTGAAAGGAATCAAAGAAATGGAGCCGTG
TATCAGGTGGGGAAGGGTGGGGGCCAAGGGGGTGTCCTTCCCCATACAGAGATTGCAGGCTGAGAATGAC
TATATCCTTGTTAACAGGAGGTGGGAGCAGGGCACGGTAGCTCACACCTGTAATCTTGGCACTTTAGGAG
GCTGAGGCGGGCCGATCACCTGAAGTAAGGAGTTCGAGACCAGCCTGGCCAACATGCAAAGCCCTGTCTC
TACTAAAAATACAAAAATTAGCTGGGTGTGGTGGTACTCGCCTGTAATCCCAGCTACTCGGGAGACTGAG
GCAGGAGAATGGCTTGAACCCGGAAGGTAGAGGTTGCAGTGAGCTGAGATCATGCCACTGTGCTCCAGCC
TAGGTGACAGAGAGAGACTCCATCTCAAAAAAAAAAAAAAAATACAGGAAGGGAGTTGGGAATAGGGTGC
ACATTTAGGAAGTCTTGGGGATTTAGTGGTGGGAAGGTTGGAAGTCCCTCTCTGATTGTCTTTTCCTCAA
AGAAGTGCATGGCTGGTGAGGGGTGGGGCAGGAGTGCTTGGGTTGTGGTGAAACATTGGAAGAGAGAATG
TGAAGCAGCCATTCTTTTCCTGCTCCACAGGAAGCCGAGCTGTCTCAGACACTGGCATGGTGTTGGGGGA
GGGGGTTCCTTCTCTGCAGGCCCAGGTGACCCAGGGTTGGAAGTGTCTCATGCTGGATCCCCACTTTTCC
TCTTGCAGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGC
CCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTGTGAGTGGATCCATTGGAAGGGCAGGCCCA
CCACCCCCACCCCAACCCCAGCCCCCTAGCAGAGACCTGTGGGAAGCGAAAATTCCATGGGACTGACTTT
CTGCTCTTGTCTTTCAGACTTCCTGAAAACAACGTTCTGGTAAGGACAAGGGTTGGGCTGGGGACCTGGA
GGGCTGGGGACCTGGAGGGCTGGGGGGCTGGGGGGCTGAGGACCTGGTCCTCTGACTGCTCTTTTCACCC
ATCTACAGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATG
GTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCA
CCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCC
AGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGAC
TTGCACGGTCAGTTGCCCTGAGGGGCTGGCTTCCATGAGACTTCAATGCCTGGCCGTATCCCCCTGCATT
TCTTTTGTTTGGAACTTTGGGATTCCTCTTCACCCTTTGGCTTCCTGTCAGTGTTTTTTTATAGTTTACC
CACTTAATGTGTGATCTCTGACTCCTGTCCCAAAGTTGAATATTCCCCCCTTGAATTTGGGCTTTTATCC
ATCCCATCACACCCTCAGCATCTCTCCTGGGGATGCAGAACTTTTCTTTTTCTTCATCCACGTGTATTCC
TTGGCTTTTGAAAATAAGCTCCTGACCAGGCTTGGTGGCTCACACCTGCAATCCCAGCACTCTCAAAGAG
GCCAAGGCAGGCAGATCACCTGAGCCCAGGAGTTCAAGACCAGCCTGGGTAACATGATGAAACCTCGTCT
CTACAAAAAAATACAAAAAATTAGCCAGGCATGGTGGTGCACACCTATAGTCCCAGCCACTTAGGAGGCT
GAGGTGGGAAGATCACTTGAGGCCAGGAGATGGAGGCTGCAGTGAGCTGTGATCACACCACTGTGCTCCA
GCCTGAGTGACAGAGCAAGACCCTATCTCAAAAAAAAAAAAAAAAAAGAAAAGCTCCTGAGGTGTAGACG
CCAACTCTCTCTAGCTCGCTAGTGGGTTGCAGGAGGTGCTTACGCATGTTTGTTTCTTTGCTGCCGTCTT
CCAGTTGCTTTATCTGTTCACTTGTGCCCTGACTTTCAACTCTGTCTCCTTCCTCTTCCTACAGTACTCC
CCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACAC
CCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAG
GCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTGAGCAGCTGGGGCTGGAGAGACGACAGGGC
TGGTTGCCCAGGGTCCCCAGGCCTCTGATTCCTCACTGATTGCTCTTAGGTCTGGCCCCTCCTCAGCATC
TTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCGACATAGTGTGGT
GGTGCCCTATGAGCCGCCTGAGGTCTGGTTTGCAACTGGGGTCTCTGGGAGGAGGGGTTAAGGGTGGTTG
TCAGTGGCCCTCCAGGTGAGCAGTAGGGGGGCTTTCTCCTGCTGCTTATTTGACCTCCCTATAACCCCAT
GAGATGTGCAAAGTAAATGGGTTTAACTATTGCACAGTTGAAAAAACTGAAGCTTACAGAGGCTAAGGGC
CTCCCCTGCTTGGCTGGGCGCAGTGGCTCATGCCTGTAATCCCAGCACTTTGGGAGGCCAAGGCAGGCGG
ATCACGAGGTTGGGAGATCGAGACCATCCTGGCTAACGGTGAAACCCCGTCTCTACTGAAAAATACAAAA
AAAAATTAGCCGGGCGTGGTGCTGGGCACCTGTAGTCCCAGCTACTCGGGAGGCTGAGGAAGGAGAATGG
CGTGAACCTGGGCGGTGGAGCTTGCAGTGAGCTGAGATCACGCCACTGCACTCCAGCCTGGGCGACAGAG
CGAGATTCCATCTCAAAAAAAAAAAAAAAAGGCCTCCCCTGCTTGCCACAGGTCTCCCCAAGGCGCACTG
GCCTCATCTTGGGCCTGTGTTATCTCCTAGGTTGGCTCTGACTGTACCACCATCCACTACAACTACATGT
GTAACAGTTCCTGCATGGGCGGCATGAACCGGAGGCCCATCCTCACCATCATCACACTGGAAGACTCCAG
GTCAGGAGCCACTTGCCACCCTGCACACTGGCCTGCTGTGCCCCAGCCTCTGCTTGCCTCTGACCCCTGG
GCCCACCTCTTACCGATTTCTTCCATACTACTACCCATCCACCTCTCATCACATCCCCGGCGGGGAATCT
CCTTACTGCTCCCACTCAGTTTTCTTTTCTCTGGCTTTGGGACCTCTTAACCTGTGGCTTCTCCTCCACC
TACCTGGAGCTGGAGCTTAGGCTCCAGAAAGGACAAGGGTGGTTGGGAGTAGATGGAGCCTGGTTTTTTA
AATGGGACAGGTAGGACCTGATTTCCTTACTGCCTCTTGCTTCTCTTTTCCTATCCTGAGTAGTGGTAAT
CTACTGGGACGGAACAGCTTTGAGGTGCGTGTTTGTGCCTGTCCTGGGAGAGACCGGCGCACAGAGGAAG
AGAATCTCCGCAAGAAAGGGGAGCCTCACCACGAGCTGCCCCCAGGGAGCACTAAGCGAGGTAAGCAAGC
AGGACAAGAAGCGGTGGAGGAGACCAAGGGTGCAGTTATGCCTCAGATTCACTTTTATCACCTTTCCTTG
CCTCTTTCCTAGCACTGCCCAACAACACCAGCTCCTCTCCCCAGCCAAAGAAGAAACCACTGGATGGAGA
ATATTTCACCCTTCAGGTACTAAGTCTTGGGACCTCTTATCAAGTGGAAAGTTTCCAGTCTAACACTCAA
AATGCCGTTTTCTTCTTGACTGTTTTACCTGCAATTGGGGCATTTGCCATCAGGGGGCAGTGATGCCTCA
AAGACAATGGCTCCTGGTTGTAGCTAACTAACTTCAGAACACCAACTTATACCATAATATATATTTTAAA
GGACCAGACCAGCTTTCAAAAAGAAAATTGTTAAAGAGAGCATGAAAATGGTTCTATGACTTTGCCTGAT
ACAGATGCTACTTGACTTACGATGGTGTTACTTCCTGATAAACTCGTCGTAAGTTGAAAATATTGTAAGT
TGAAAATGGATTTAATACACCTAATCTAAGGAACATCATAGCTTAGCCTAGCCTGCTTTTTTTTTTTTTT
TTTTTGGAGACAGAGTCTCACTCTGTCACCCAGGCTGGAGTGCAGTGGCGGGATCTCGGCTCACTGCAAC
CTCCGCCTTCTGGGTTCAAGCGATTCTCCTGCCTCAGCCCACTGAGTAGCTGGGATTACAGGCACCTGCC
CCGACGCCCAGCTAATTTTTTGTTATTTATTTATTTTTTTTTTTAGTAGAGATGAGGTTTCACCATGTTG
GCCAGGCTAGTCTCGAACTCCTGACCTTGTGATCTGCCTGCCTTGGCCTCCCAAAGTGCTGGGATTACAG
GCGTGAGCCACCGCACCCGGCCTGCCTAGCCTACTTTTATTTTATTTTTAATGGAGACAGCATCTTGCTC
TGTTGCCCAGGCTGGATTACAGTGATGTGATCATAGCTCATTATACCCTCCTGGGCTCAAGCAATCCCCC
TAACTCTGCCTCCCCAGTAGCTAGGACCACAGGCATACACCACCATACCCAGCTAATTTTTAAAATTTTT
TGTAGATAGATAGAGTCTCACTATGTTGCCCAGGCTGGTCTCTAGCCTACTTTTTTGAGACAAGGTCTTG
CTCTGTCACCCAGGCTGGATAGAGTGCAGTAGTGCAGTCACAGCTCACTGCAGCCTCCACCTCCCAGGCT
CCATCCATCCTCCCAGCTCAGCCTCCCAAGTTGCTTCAACTACAGGCCTGCACCACCATGCCTGGCTAAT
TTTTATTTATTTATTTTTATTTTATTTTATTTTATTTTTTTGAGACTCAGTCTCACTCTGTCGCCCAGGC
TGGAGTGCAGTGGCATGATCTCGGCTCACTGCAACCTCTGCCTCCTGGGTTCAAGTGATTCTCCTGCCTC
AGCCTCCCGAATAGCTAGGACTACAAGCGCCTGCTACCACGCCCAGCTAATTTTTGTATTTTTAGTAGAG
ACAGGGTTTCACCATGTTGGCCAGGCTGGTCTCGAACTTCTGACCATGTGATCCGCCCGCCTCGGCCTCC
CAAAGTGCTGGGATTACAGGTGTGAGCCACCACGCCCGGCTAATTTTTATTTATTTATTTAAAGACAGAG
TCTCACTCTGTCACTCAGGCTAGAGTGCAGTGGCACCATCTCAGCTCACTGCAGCCTTGACCTCCCTGGG
CTCCGGTGATTTCACCCTCCCAAGTAGCTAGGACTACAGGCACATGCCACGACACCCAGCTAATTTTTTA
TTTTCTGTGAAGTCAAGGTCTTGCTACGTTGCCCATGCTGGTATCAAACCCCTGGGCTCAATCAATCCTT
CCACCTCAGCCTCCCCAAGTATTGGGGTTACAGGCATGAGCTACCACACTCAGCCCTAGCCTACTTGAAA
CGTGTTCAGAGCATTTAAGTTACCCTACAGTTGGGCAAAGTCATCTAACACAAAGCCCTTTTTATAGTAA
TAAAATGTTGTATATCTCATGTGATTTATTGAATATTGTTACTGAAAGTGAGAAACAGCATGGTTGCATG
AAAGGAGGCACAGTCGAGCCAGGCACAGCCTGGGCGCAGAGCGAGACTCAAAAAAAGAAAAGGCCAGGCG
CACTGGCTCACGCCTGTAATCCCAGCATTTCGGGAGGCTGAGGCGGGTGGATCACCTGAGGTCAGGAGTT
CAAGACCAGCCTAGCCAACATGGTGAAACCCCGTCTCTACTAAAATACAAAAATTAACCGGGCGTGATGG
CAGGTGCCTGTAATCCCAGCTACTTGGGAGGCTGAGGCAGGAGAATCGCTTGAACCAGGAGGCGGAGGTT
GCAGGGAGCCAAGATGGCGCCACTGCACTCCAGCCTGGGCGATAGAGTGAGACTCCGTCTCAGAAAAAAA
AGAAAAGAAACGAGGCACAGTCGCATGCACATGTAGTCCCAGTTACTTGAGAGGCTAAGGCAGGAGGATC
TCTTGAGCCCAAGAGTTTGAGTCCAGCCTGAACAACATAGCAAGACATCATCTCTAAAATTTAAAAAAGG
GCCGGGCACAGTGGCTCACACCTGTAATCCCAGCACTTTGGGAGGTGGAGGTGGGTAGATCACCTGACGT
CAGGAGTTGGAAACCAGCCTGGCTAACATGGTGAAGCCCCATCTCTACTAAAAACACAAAAATTAGCCAG
GTGTGGTAGCACACGCCTGTAGTCCCAGCTACTCGGGAGGCTGAGGCACAAGAATCACTTGAACCCCAGA
GGCGGAGATTGCAATCAGCCAAGATTGCACCATTGCACTCCCGCCTGGGCAACAGAGTGAGACCCCATCT
CAAAATAAATAAATAAATATTTTTAAAAGTCAGCTGTATAGGTACTTGAAGTGCAGTTTCTACTAAATGC
ATGTTGCTTTTGTACCGTCATAAAGTCAAACAATTGTAACTTGAACCATCTTTTAACTCAGGTACTGTGT
ATATACTTACTTCTCCCCCTCCTCTGTTGCTGCAGATCCGTGGGCGTGAGCGCTTCGAGATGTTCCGAGA
GCTGAATGAGGCCTTGGAACTCAAGGATGCCCAGGCTGGGAAGGAGCCAGGGGGGAGCAGGGCTCACTCC
AGGTGAGTGACCTCAGCCCCTTCCTGGCCCTACTCCCCTGCCTTCCTAGGTTGGAAAGCCATAGGATTCC
ATTCTCATCCTGCCTTCATGGTCAAAGGCAGCTGACCCCATCTCATTGGGTCCCAGCCCTGCACAGACAT
TTTTTTAGTCTTCCTCCGGTTGAATCCTATAACCACATTCTTGCCTCAGTGTATCCACAGAACATCCAAA
CCCAGGGACGAGTGTGGATACTTCTTTGCCATTCTCCGCAACTCCCAGCCCAGAGCTGGAGGGTCTCAAG
GAGGGGCCTAATAATTGTGTAATACTGAATACAGCCAGAGTTTCAGGTCATATACTCAGCCCTGCCATGC
ACCGGCAGGTCCTAGGTGACCCCCGTCAAACTCAGTTTCCTTATATATAAAATGGGGTAAGGGGGCCGGG
CGCAGTGGCTCACGAATCCCACACTCTGGGAGGCCAAGGCGAGTGGATCACCTGAGGTCGGGAGTTTGAG
CCCAGCCTGACCAACATGGAGAAACCCCATCTCTACTAAAAATACAAAAGTAGCCGGGCGTGGTGATGCA
TGCCTGTAATCCCAGCTACCTACTCGGGAGGCTGAGGCAGGAGAATCGCTTGAACCCGGGAGGCAGAGGT
TGCGGTGAGCTGAGATCTCACCATTACACTCCAGCCTGGGCAACAAGAGTGAAACTCCGTCTCAAAAAAG
ATAAATAAAGTAAAATGGGGTAAGGGAAGATTACGAGACTAATACACACTAATACTCTGAGGTGCTCAGT
AAACATATTTGCATGGGGTGTGGCCACCATCTTGATTTGAATTCCCGTTGTCCCAGCCTTAGGCCCTTCA
AAGCATTGGTCAGGGAAAAGGGGCACAGACCCTCTCACTCATGTGATGTCATCTCTCCTCCCTGCTTCTG
TCTCCTACAGCCACCTGAAGTCCAAAAAGGGTCAGTCTACCTCCCGCCATAAAAAACTCATGTTCAAGAC
AGAAGGGCCTGACTCAGACTGACATTCTCCACTTCTTGTTCCCCACTGACAGCCTCCCACCCCCATCTCT
CCCTCCCCTGCCATTTTGGGTTTTGGGTCTTTGAACCCTTGCTTGCAATAGGTGTGCGTCAGAAGCACCC
AGGACTTCCATTTGCTTTGTCCCGGGGCTCCACTGAACAAGTTGGCCTGCACTGGTGTTTTGTTGTGGGG
AGGAGGATGGGGAGTAGGACATACCAGCTTAGATTTTAAGGTTTTTACTGTGAGGGATGTTTGGGAGATG
TAAGAAATGTTCTTGCAGTTAAGGGTTAGTTTACAATCAGCCACATTCTAGGTAGGGGCCCACTTCACCG
TACTAACCAGGGAAGCTGTCCCTCACTGTTGAATTTTCTCTAACTTCAAGGCCCATATCTGTGAAATGCT
GGCATTTGCACCTACCTCACAGAGTGCATTGTGAGGGTTAATGAAATAATGTACATCTGGCCTTGAAACC
ACCTTTTATTACATGGGGTCTAGAACTTGACCCCCTTGAGGGTGCTTGTTCCCTCTCCCTGTTGGTCGGT
GGGTTGGTAGTTTCTACAGTTGGGCAGCTGGTTAGGTAGAGGGAGTTGTCAAGTCTCTGCTGGCCCAGCC
AAACCCTGTCTGACAACCTCTTGGTGAACCTTAGTACCTAAAAGGAAATCTCACCCCATCCCACACCCTG
GAGGATTTCATCTCTTGTATATGATGATCTGGATCCACCAAGACTTGTTTTATGCTCAGGGTCAATTTCT
TTTTTCTTTTTTTTTTTTTTTTTTCTTTTTCTTTGAGACTGGGTCTCGCTTTGTTGCCCAGGCTGGAGTG
GAGTGGCGTGATCTTGGCTTACTGCAGCCTTTGCCTCCCCGGCTCGAGCAGTCCTGCCTCAGCCTCCGGA
GTAGCTGGGACCACAGGTTCATGCCACCATGGCCAGCCAACTTTTGCATGTTTTGTAGAGATGGGGTCTC
ACAGTGTTGCCCAGGCTGGTCTCAAACTCCTGGGCTCAGGCGATCCACCTGTCTCAGCCTCCCAGAGTGC
TGGGATTACAATTGTGAGCCACCACGTCCAGCTGGAAGGGTCAACATCTTTTACATTCTGCAAGCACATC
TGCATTTTCACCCCACCCTTCCCCTCCTTCTCCCTTTTTATATCCCATTTTTATATCGATCTCTTATTTT
ACAATAAAACTTTGCTGCCACCTGTGTGTCTGAGGGGTG"

