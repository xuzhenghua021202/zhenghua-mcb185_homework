# 1 high probability  error or probability not correct
# 5 low probability error
import math

def char_to_prob(char): 
	q_score = ord(char) - 49
	if q_score < 0:
		return None
	
	return 10 ** (- q_score - 1)
	
def prob_to_char(prob):
	q_score = -1 * math.log10(prob) -1 
	return chr(int(round(q_score)) + 49)
		


print(char_to_prob('5')) # suppose to be 0.1

print(prob_to_char(0.1)) # suppose to be 5 

		 
	