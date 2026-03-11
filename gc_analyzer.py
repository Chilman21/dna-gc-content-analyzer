import numpy as np

dna_sequence = "ATGCGCGTAACGTTAGCGCGATTA"

sequence_array = np.array(list(dna_sequence))

A_count = np.sum(sequence_array == 'A')
T_count = np.sum(sequence_array == 'T')
G_count = np.sum(sequence_array == 'G')
C_count = np.sum(sequence_array == 'C')

total = len(sequence_array)

gc_content = ((G_count + C_count) / total) * 100

print("DNA Sequence:", dna_sequence)
print("Length:", total)

print("A:", A_count)
print("T:", T_count)
print("G:", G_count)
print("C:", C_count)

print("GC Content:", gc_content, "%")
