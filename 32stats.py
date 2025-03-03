import math
import sys

main = []
for arg in sys.argv[1:]: 
	f = float(arg)
	if len(sys.argv) < 2: sys.exit('error: no nuhmbers provided')
	main.append(f)
	
print(f'{len(main)}')


mini = main[0]
maxi = main[0]
for num in main:
	if num < mini: 
		mini = num
	if num > maxi: 
		maxi = num
		
print(f'Minimum value:{mini}')
print(f'Maximum value:{maxi}')


total = 0
for val in main: total += val
mean_value = total / len(main)

print(f'mean value:{mean_value:f}')
	
variance = sum((x - mean_value) ** 2 for x in main) / len(main)
std_dev = math.sqrt(variance)
print(f'Standard Deviation: {std_dev:f}')

sorted_main = sorted(main)
n = len(sorted_main)
if n % 2 ==1:
	median = sorted_main[n // 2]
else: 
	median = (sorted_main[n // 2-1] + sorted_main[n // 2]) / 2

print(f'Median value: {median:f}')

