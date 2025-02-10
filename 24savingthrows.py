import math

import random


def advantage():
	roll1 = random.randint(1, 20)
	roll2 = random.randint(1, 20)
	if roll1 > roll2: return roll1 
	return roll2
	
def disadvantage():
	roll1 = random.randint(1, 20)
	roll2 = random.randint(1, 20)
	if roll1 < roll2:
		return roll1
	return roll2
	
trials = 100000
dc = 5
size = 5
for dc in range(5, 10 ,15):
	nor = 0
	adv = 0
	dis = 0
	
	for i in range(trials): 
		r1 = random.randint(1, size)
		r2 = random.randint(1, size)
		if r1 >= dc: nor += 1
		if r1 >= dc and r2 >= dc: dis += 1
		if r1 >= dc or r2 >= dc: adv += 1
print(dc, nor/trials, adv/trials, dis/trials)

