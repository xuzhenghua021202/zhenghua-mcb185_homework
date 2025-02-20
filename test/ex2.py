def is_prime(n): 
	for d in range(2, n): 
		r = n % d
		if r == 0: return False
	return True

for i in range (51, 0, -2): 
	if is_prime(i):  print(i, "*")
	else: print(i)