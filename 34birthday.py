import random

import sys


trials = int(sys.argv[1])
students = int(sys.argv[2])
shared = 0


for t in range(trials):
	peeps = []
	collision = False
	
	for i in range(students):
		bday= random.randint(0, 364)
		if bday in peeps:
			collision = True
			break
		peeps.append(bday)
	if collision: 
		shared += 1
			
print(shared/float(trials))



