import sys

alphabet = sys.argv[1]
match_score = int(sys.argv[2])
mismatch_score = int(sys.argv[3])


alphabet_list = list(alphabet)


print("   " + " ".join(alphabet_list))


for i in range(len(alphabet_list)): 
    row = [alphabet_list[i]]  
    for j in range(len(alphabet_list)): 
        if alphabet_list[i] == alphabet_list[j]:
            row.append(f"{match_score:+}")  
        else:
            row.append(f"{mismatch_score:+}")
    print(" ".join(row))
