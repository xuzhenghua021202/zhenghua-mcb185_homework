import sys
import math
import mcb185

fasta_file = sys.argv[1]
w = int(sys.argv[2]) 
et = float(sys.argv[3]) 

def entropy(win):
	a = win.count('A') / len(win)
	c = win.count('C') / len(win)
	g = win.count('G') / len(win)
	t = win.count('T') / len(win)
	h = 0 
	for freq in [a, t, c, g]:
		if freq > 0:
			h += freq * math.log2(freq)
	return -h

for defline, seq in mcb185.read_fasta(fasta_file):
	mask = list(seq)
	for i in range(len(seq) - w + 1):
		window = seq[i:i + w]
		if entropy(window) < et:
			for j in range(i, i + w):
				mask[j] = 'N'
	print(defline)
	mask_seq = ''.join(mask)
	for i in range(0, len(mask_seq), 60):
		print(mask_seq[i:i + 60])