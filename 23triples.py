import math 

limit = 100
for a in range(1, limit):
	for b in range(a + 1, limit):
		c = math.sqrt(a **2 + b **2)
		remainder = c % 1 
		if remainder == 0: print(a, b, c)
	
	

	