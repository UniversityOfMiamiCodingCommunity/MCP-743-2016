fileInput = open("/Users/Chris/Documents/Chris/python/MCP-743/dataFiles/cd_antigen.txt", "r")
Entry_names = []
Protein_names = []
Gene_names = []
Organisms = []
i = 0
for line in fileInput:
    cell_markers = line.split("\t")
    Entry_names.append(cell_markers[1])
    Protein_names.append(cell_markers[3])
    Gene_names.append(cell_markers[4])
    Organisms.append(cell_markers[5])

combined_results = [('Entry name: ' + Entry_names[i], 'Protein name: ' + Protein_names[i], 'Gene name: ' + Gene_names[i], 'Organism: ' + Organisms[i]) for i in range(len(Entry_names))]
for result in combined_results:
    print(result, '\n')
for Gene_name in Gene_names:
    cd_antigens = []
    if 'CD' in Gene_name:
        cd_antigens.append(Gene_name)
        print(cd_antigens)