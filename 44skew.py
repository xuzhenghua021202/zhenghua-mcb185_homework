import gzip
import sys
import sequence
fasta_file = sys.argv[1]
w = int(sys.argv[2])



with gzip.open(fasta_file, 'rt') as fp:
	seq_list = []
	for line in fp: 
		if line.startswith('>'):
			continue
		seq_list.append(line.strip())
seq = ' '.join(seq_list)
		

for i in range(len(seq) - w + 1):
	w_seq = seq[i:i+w]
	gc_count = sequence.gc_comp(w_seq)
	gc_skewval = sequence.gc_skew(w_seq)
	print(i, gc_count,gc_skewval)

import sys
import gzip
fasta_file = sys.argv[1]
w = int(sys.argv[2])

with gzip.open(fasta_file,'rt') as fp:
	seq = ""
	for line in fp: 
		if line.startswith('>'):
			continue
		seq += line.strip()
for i in range(len(seq) - w + 1):
	w_seq = seq[i:i+w]
	gc_content = sequence.gc_comp(w_seq)
	gc_skew_val = sequence.gc_skew(w_seq)
	print(i, gc_content, gcskew_val)
			