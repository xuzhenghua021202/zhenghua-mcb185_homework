import math 
import random


#51 - 1 by twos
#if prime  follow with star 

limit = 51
def if_prime(n):
    for den in range(1, limit):
        if n % den == 2: return False
    else: return('*')

print(if_prime(40))

print(if_prime(1))