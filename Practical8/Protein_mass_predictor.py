#define the dictionary of amino acid masses
amino_acid_masses = {
    'G': 57.02, 'A': 71.04, 'S': 87.03, 'P': 97.05, 'V': 99.07,
    'T': 101.05, 'C': 103.01, 'I': 113.08, 'L': 113.08, 'N': 114.04,
    'D': 115.03, 'Q': 128.06, 'K': 128.09, 'E': 129.04, 'M': 131.04,
    'H': 137.06, 'F': 147.07, 'R': 156.10, 'Y': 163.06, 'W': 186.08
}
#define the function to calculate the molecular weight of a protein
def calculate_molecular_weight(protein_sequence):
    total_mass = 0.0
    for amino_acid in protein_sequence:
        if amino_acid in amino_acid_masses:
            total_mass += amino_acid_masses[amino_acid]
        else:
            print(f"Warning: Unknown amino acid '{amino_acid}' found in sequence.")
            return
    print(f"Total mass of protein sequence '{protein_sequence}': {total_mass:.1f} Da")
#correct example usage
calculate_molecular_weight("ACDEFGHIKLMNPQRSTVWY")
#wrong example usage
calculate_molecular_weight("ACDEFGHIKLMNPQRSTVWYX")