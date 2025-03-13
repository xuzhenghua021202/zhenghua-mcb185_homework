import sys
import mcb185
fasta_file = sys.argv[1]

	
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
	signal = False
	trans = False
	if len(seq) >= 30:
		N_term = seq[:30]
		c_term = seq[30:]
	
		for i in range(0, len(N_term) - 7):
			peptide = N_term[i:i+8]
			if  kd(peptide) >=2.5 and "P" not in peptide:
				signal = True
				break
		for i in range(0, len(c_term) - 10, 1):
			region = c_term[i:i+11]
			if not kd(region) >= 2.0 and "P" not in peptide:
				trans = True
				break
		
		if signal and trans:

			print(defline)

