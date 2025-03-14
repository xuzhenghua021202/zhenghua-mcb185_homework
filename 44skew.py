import mcb185
import sys
import sequence
w = int(sys.argv[2])



for defline, seq in mcb185.read_fasta(sys.argv[1]): 

	for i in range(len(seq) - w + 1):
		w_seq = seq[i:i+w]
		gc_count = sequence.gc_comp(w_seq)
		gc_skewval = sequence.gc_skew(w_seq)
		print(i, gc_count,gc_skewval)

import sys

w = int(sys.argv[2])

for defline, seq in mcb185.read_fasta(sys.argv[1]): 

	for i in range(len(seq) - w + 1):
		w_seq = seq[i:i+w]
		gc_content = sequence.gc_comp(w_seq)
		gc_skew_val = sequence.gc_skew(w_seq)
		print(i, gc_content, gcskew_val)
				