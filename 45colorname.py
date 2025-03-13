import sys

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])


def dtc(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += abs(p - q)
	return d
	
mini_dis = float('inf')
closest_color = None


with open(colorfile, 'r') as file: 
	for line in file: 
		if line.startswith('#'):
			continue
	
		parts = line.strip().split('\t')
		name = parts[0]
		rgb_value = parts[2].split(',')
		r = int(rgb_value[0])
		g = int(rgb_value[1])
		b = int(rgb_value[2])
		distance = dtc((R, G, B), (r, g, b))
	
		if distance < mini_dis:
			closest_color = name 
			mini_dis = distance
			

	print(closest_color, distance)
	