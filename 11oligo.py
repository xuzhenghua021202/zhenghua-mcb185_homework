def tm(a, c, g, t):
	length = a + c + g + t
	if length <= 13:
		return 3
	
	if length <= 13: 
		temp = (a + t) * 2 + (g + c) * 4
		return temp 
	
	else: 
		temp = 64.9 + 41 * (g + c - 16.4 ) / length
		return temp
		
t = tm(5, 7, 3, 4)
print(tm(5, 7, 3, 4))
	