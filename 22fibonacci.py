import math 

trials = 10
x = 0
y = 1
for i in range(trials): 
	
	print('trials', x, end=" ")
	new = x + y
	x = y
	y = new
