#find start and stop codons
start_codon = "ATG"
stop_codons = {"TAA", "TAG", "TGA"}
#input sequence
input_file="C:\\Users\\24367\\Desktop\\GITHUB\\IBI1_2025-26\\Practical7\\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_file="C:\\Users\\24367\\Desktop\\GITHUB\\IBI1_2025-26\\Practical7\\stop_genes.fa"
valid_genes = []
current_name = None
current_sequence = ""
#open file
with open(input_file, "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue#skip empty lines
        if line.startswith(">"):
            if current_name is not None and current_sequence!="":#handle the previous genes
                seq=current_sequence
                stops_in_frame=set()
                #look for the first ATG
                atg_pos=-1
                for i in range(len(seq)-2):
                    codon=seq[i:i+3]
                    if codon==start_codon:
                        atg_pos=i
                        break
                #read from the first ATG and check for stop codons in frame
                if atg_pos!=-1:
                    for j in range(atg_pos+3, len(seq)-2, 3):
                        codon=seq[j:j+3]
                        if codon in stop_codons:
                            stops_in_frame.add(codon)
                if len(stops_in_frame)>0:
                    valid_genes.append((current_name, current_sequence, stops_in_frame))
            current_name = line.split()[0][1:]  # get the gene name without '>'
            current_sequence = ""
        else:
            current_sequence += line

    if current_name is not None and current_sequence!="":
        seq=current_sequence
        stops_in_frame=set()
        atg_pos=-1
        for i in range(len(seq)-2):
            codon=seq[i:i+3]
            if codon==start_codon:
                atg_pos=i
                break
        if atg_pos!=-1:
            for j in range(atg_pos+3, len(seq)-2, 3):
                codon=seq[j:j+3]
                if codon in stop_codons:
                    stops_in_frame.add(codon)
        if len(stops_in_frame)>0:
            valid_genes.append((current_name, current_sequence, stops_in_frame))
with open(output_file, "w") as f:
    for name, seq, stops in valid_genes:
        stop_str = " ".join(sorted(stops))
        f.write(f">{name} {stop_str}\n")
        for i in range(0, len(seq), 80):
             f.write(seq[i:i+80] + "\n")
print(f"Stopped genes written to {output_file} with {len(valid_genes)} valid genes found.")
