#define the sequence
sequence = "AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG"
#start codon
start_codon = "AUG" 
#stop codons
stop_codons = {"UAA", "UAG", "UGA"}
#find the start and stop codons
#find the largest ORF
orf_dic={}
for i in range(len(sequence) - 2):
    if sequence[i:i+3] == start_codon:
        # check 3 bases at a time for stop codon
        for j in range(i + 3, len(sequence) - 2, 3):
            codon = sequence[j:j+3]
            if codon in stop_codons:
                # get the ORF sequence
                orf_seq = sequence[i:j+3]
                # calculate length
                orf_len = len(orf_seq)
                # store in dictionary (length as key)
                orf_dic[orf_len] = orf_seq
                break  # stop searching for this ORF after finding the first stop codon

#find the largest ORF
if orf_dic:
   max_len = max(orf_dic.keys())
   longest_orf = [seq for length, seq in orf_dic.items() if length == max_len]
   print(f"the longest ORF length is {max_len} and there are {len(longest_orf)}")
   for i, seq in enumerate(longest_orf, 1):
       print(f"ORF {i}: {seq}")
else:   print("No ORF found.")