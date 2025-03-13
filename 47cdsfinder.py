import sys
import mcb185

# Parse command-line arguments
fasta_file = sys.argv[1]
min_length = int(sys.argv[2])

orf_id = 0  # Initialize ORF counter

# Read FASTA file
for defline, seq in mcb185.read_fasta(fasta_file):
    # Process both forward and reverse complement strands
    for nt_seq in [seq, mcb185.anti_seq(seq)]:
        for frame in range(3):  # Three reading frames
            protein = mcb185.translate(nt_seq[frame:])
            start = None  # Track start of ORF

            for i, aa in enumerate(protein):
                if aa == 'M' and start is None:
                    start = i  # ORF start
                elif aa == '*' and start is not None:
                    orf_seq = protein[start: i+1]  # Include stop codon

                    if len(orf_seq) >= min_length:
                        print('>' + defline.split()[0] + '-prot-' + str(orf_id))  # Format ORF header
                        print(orf_seq)
                        orf_id += 1  # Increment ORF count

                    start = None  # Reset ORF start for next sequence
