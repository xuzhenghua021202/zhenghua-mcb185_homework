s = 'hello world'
print(s)

s1 = 'hey "dude"'
s2 = "don't tell me what to do"
print(s1, s2)

print('hey "dude" don\'t tell me what to do')

print(s.upper())
print(s1)

print(s.endswith(s1))

print(s.replace('o', ''))
print(s.replace('o', '').replace('r', 'i'))

import math
print(f'{math.pi}')            # does nothing special
print(f'{math.pi:.3f}')        # 3 fixed digits after decimal
print(f'{1e6 * math.pi:e}')    # exponent notation
print(f'{"hello world":>20}')  # right justify with space filler
print(f'{"hello world":.>20}') # right justify with dot filler
print(f'{20:<10} {10}')        # left justify

print('{} {:.3f}'.format('str.format', math.pi))

print('%s %.3f' % ('printf', math.pi))
print('%s %.4f' % ('printf', math.pi))

seq = 'GAATTC'
print(seq[0],seq[1])
print(seq[-1])

for nt in seq: 
	print(nt, end='')
print()

for i in range(len(seq)):
	print(i, seq[i])
	
	
s = 'ABCDEFGHIJ'
print(s[0:5])
print(s[0:8:2])
print(s[0:5], s[:5])
print(s[5:len(s)], s[5:])
print(s, s[::], s[::1], s[::-1])

dna = 'ATGCTGTAA'
for i in range(0, len(dna), 3):
	codon = dna[i:i+3]
	print(i, codon)

tax = ('Homo', 'sapiens', 9606)
print(tax)

nts = 'ACGT'
for i in range (len(nts)):
	print(i, nts[i])

for i, nt in enumerate(nts):
	print(i, nt)

names = ('adenine', 'cytosine', 'guanine', 'thyminr')
for i in range(len(names)):
	print(nts[i], names[i])
for nt, name in zip(nts, names):
	print(nt, name)
for i, (nt, name) in enumerate(zip(nts, names)):
	print(i, nt, name)
	
nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)
nts.append('C')
print(nts)

last = nts.pop()
print(last)

nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)

nucleotides = nts
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)

items = list()
print(items)
items.append('eggs')
print(items)

stuff = []
stuff.append(3)
print(stuff)

alph = 'ACDEFGHIKLMPQRSVW'
print(alph)
aas = list(alph)
print(aas)


text = 'good day			to you'
word = text.split()
print(word)

line = '1.41, 2.72, 3.14'
print(line.split(','))
s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)

if 'A' in alph: print('yay')
if 'a' in alph: print('no')


print('find G?', alph.find('G'))
print('find Z?', alph.find('Z'))

import sys
print(sys.argv)

i = int('42')
x = float('hello')
print(i * x)