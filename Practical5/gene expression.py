gene_expression = {"TP53": 12.4,
                  "EGFR": 15.1,
                  "BRCA1": 8.2,
                  "PTEN": 5.3,
                  "ESR1": 10.7}
print("original dictionary", gene_expression)
gene_expression["MYC"] = 11.6
print("updated dictionary", gene_expression)
import numpy as np
import matplotlib.pyplot as plt
N=len(gene_expression)
genes = list(gene_expression.keys())
expression = list(gene_expression.values())
plt.figure(figsize=(8, 4))
plt.bar(genes, expression, color="skyblue")
plt.xlabel("Genes")
plt.ylabel("Expression Level")
plt.title("Gene Expression Levels")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()
gene_of_interest = "TP53"
if gene_of_interest in gene_expression:
    print(f"Expression level of {gene_of_interest}: {gene_expression[gene_of_interest]}")
else:
    print(f"{gene_of_interest} not found in the gene expression data.")
avergage_expression = np.mean(list(gene_expression.values()))
print(f"Average expression level: {average_expression}")
