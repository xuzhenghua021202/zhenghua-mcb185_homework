# 

import sys
import mcb185
fasta_file = sys.argv[1]

def trans_region(seq, w, t):
	for i in range(len(seq) - w + 1):
		segment= seq[i:i+w]
		if kd(segment) >= t and 'P' not in the peptide:
			return True
	return False
	
kd_scale = {
    'I': 4.5, 'V': 4.2, 'L': 3.8, 'F': 2.8, 'C': 2.5, 'M': 1.9, 
    'A': 1.8, 'G': -0.4, 'T': -0.7, 'S': -0.8, 'W': -0.9, 'Y': -1.3, 
    'P': -1.6, 'H': -3.2, 'E': -3.5, 'Q': -3.5, 'D': -3.5, 'N': -3.5, 'K': -3.9, 'R': -4.5
}
def kd(seq):
	if len(seq) ==0:
		return 0
	total = 0
	for aa in seq:
		if aa in kd_scale:
			total += kd_scale[aa]
	return total/ len(seq)

for defline, seq in mcb185.read_fasta(fasta_file):
	if trans_region(seq[:30], 8, 2.5) and trans_region(seq[30:], 11, 2.0):
		print(defline)
	
