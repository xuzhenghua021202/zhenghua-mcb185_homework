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
		
