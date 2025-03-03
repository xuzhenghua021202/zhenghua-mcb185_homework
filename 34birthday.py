import sys
import random


trials = int(sys.argv[1])
days = int(sys.argv[2])
students = int(sys.argv[3])

shared = 0

for t in range(trials):
	calendar = [0] * days 
		
	for s in range(students):
		bdays = random.randint(0, days-1)	
		calendar[bdays] += 1
	
	for c in range(len(calendar)):
		if calendar[c] > 1:
			shared += 1
			break 

print(shared / trials)
	

