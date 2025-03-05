import sys
import random


trials = int(sys.argv[1])
days = int(sys.argv[2])
students = int(sys.argv[3])
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
			
print(shared/trials)

