# make a function of the prob distribution
import math

def is_probdist(probs):
	total = 0
	for p in probs:
		if p < 0 or p > 1:
			return False
		total += p
	return math.isclose(total, 1)

print(is_probdist([0.5, 0.5, 1]))

import sys

alphabet = sys.argv[1]
match_score = sys.argv[2]
mismatch_score = sys.argv[3]

print('   ', end='')
for nt in alphabet: 
	print(nt, end='  ')
print()

for C1 in alphabet: 
	print(C1, end= ' ')
	for C2 in alphabet: 
		if C2 == C1:
			print(match_score, end=' ')
		else:
			print(mismatch_score, end=' ')
	print()