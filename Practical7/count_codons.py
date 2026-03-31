# Import required libraries
import os
import matplotlib.pyplot as plt
from collections import defaultdict

# Define core parameters (start/stop codons)
START_CODON = "ATG"
ALL_STOP_CODONS = {"TAA", "TAG", "TGA"}

# File paths (same as your stop_codons.py, no need to modify)
INPUT_FILE = "C:\\Users\\24367\\Desktop\\GITHUB\\IBI1_2025-26\\Practical7\\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
PIECHART_OUTPUT = "C:\\Users\\24367\\Desktop\\GITHUB\\IBI1_2025-26\\Practical7\\codon_frequency_pie.png"

# Initialize a default dictionary to count codon frequencies (auto-initialize to 0)
codon_frequency = defaultdict(int)

# Step 1: Get and validate user input for target stop codon
print("Please enter one of the stop codons (TAA, TAG, TGA) for analysis:")
while True:
    target_stop = input("> ").strip().upper()
    if target_stop in ALL_STOP_CODONS:
        print(f"Valid input: {target_stop}. Starting codon frequency analysis...\n")
        break
    else:
        print("Error! Invalid stop codon. Please enter only TAA, TAG or TGA:")

# Step 2: Read FASTA file and process each gene sequence
current_gene_name = None
current_sequence = ""

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        # Skip empty lines
        if not line:
            continue
        # Process header line (start with ">")
        if line.startswith(">"):
            # Analyze the previous gene if data is available
            if current_gene_name is not None and current_sequence != "":
                seq = current_sequence
                atg_position = -1
                # Find the first ATG start codon
                for i in range(len(seq) - 2):
                    if seq[i:i+3] == START_CODON:
                        atg_position = i
                        break
                # Only proceed if ATG is found (in-frame analysis)
                if atg_position != -1:
                    target_stop_positions = []
                    # Collect all positions of the target stop codon (in-frame)
                    for j in range(atg_position + 3, len(seq) - 2, 3):
                        codon = seq[j:j+3]
                        if codon == target_stop:
                            target_stop_positions.append(j)
                    # Use the LAST target stop codon for longest ORF
                    if target_stop_positions:
                        final_stop_pos = target_stop_positions[-1]
                        # Count all in-frame codons from ATG to final stop codon (exclude stop codon)
                        for k in range(atg_position, final_stop_pos, 3):
                            codon = seq[k:k+3]
                            codon_frequency[codon] += 1
            # Extract gene name (remove ">" and take the first part)
            current_gene_name = line.split()[0][1:]
            current_sequence = ""
        # Concatenate sequence lines (non-header lines)
        else:
            current_sequence += line
    # Process the LAST gene in the FASTA file (no subsequent ">" to trigger processing)
    if current_gene_name is not None and current_sequence != "":
        seq = current_sequence
        atg_position = -1
        for i in range(len(seq) - 2):
            if seq[i:i+3] == START_CODON:
                atg_position = i
                break
        if atg_position != -1:
            target_stop_positions = []
            for j in range(atg_position + 3, len(seq) - 2, 3):
                codon = seq[j:j+3]
                if codon == target_stop:
                    target_stop_positions.append(j)
            if target_stop_positions:
                final_stop_pos = target_stop_positions[-1]
                for k in range(atg_position, final_stop_pos, 3):
                    codon = seq[k:k+3]
                    codon_frequency[codon] += 1

# Step 3: Print codon count results to the console
print("=" * 50)
print(f"Codon Frequency Results (Upstream of {target_stop}, Longest ORF)")
print("=" * 50)
# Sort codons by frequency (highest to lowest) for readability
sorted_codons = sorted(codon_frequency.items(), key=lambda x: x[1], reverse=True)
for codon, count in sorted_codons:
    print(f"{codon}: {count} occurrences")
# Calculate total number of counted codons
total_codons = sum(codon_frequency.values())
print("=" * 50)
print(f"Total number of in-frame codons counted: {total_codons}")
print("=" * 50)

# ==============================================

# Set plot style for clarity
plt.style.use('default')
# Extract labels (codons) and sizes (counts) for the pie chart
labels = [codon for codon, cnt in sorted_codons]
sizes = [cnt for codon, cnt in sorted_codons]


fig, ax = plt.subplots(figsize=(16, 16))

# Plot pie chart: 【核心修改2：所有字体缩小，调整标签距离】
wedges, texts, autotexts = ax.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90,
    labeldistance=1.02,  
    textprops={'fontsize': 7}  
)


for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(6)  

ax.set_title(
    f'In-frame Codon Frequency Distribution (Upstream of {target_stop})\nLongest ORF from S. cerevisiae cDNA',
    fontsize=12,
    fontweight='bold',
    pad=20
)
# Ensure the pie chart is a perfect circle
ax.axis('equal')
# Save the pie chart to file (high resolution, no extra white space)
plt.tight_layout()
plt.savefig(PIECHART_OUTPUT, dpi=300, bbox_inches='tight')
plt.close()  # Close the plot to free memory

# Final success message
print(f"\nAnalysis completed successfully!")
print(f"Pie chart saved to: {PIECHART_OUTPUT}")