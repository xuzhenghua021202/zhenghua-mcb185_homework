import math 
def char_to_prob(char):
	q_score = ord(char) - 33
	if q_score < 0:
		return None
	
	return 10 ** (-q_score / 10)

def prob_to_char(prob): 
	q_score = -10 * math.log10(prob)
	if q_score < 0: 
		return None
		
	return chr(round(q_score) + 33)
		

	

print(char_to_prob('A'))
print(prob_to_char(0.001))

