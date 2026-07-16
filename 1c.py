from itertools import combinations
list=[-1,2.7,-3,4,2.5]
print("Positive combination")
for r in range(1, len(list)+1):
    for combo in combinations(list, r):
        if all(x > 0 for x in combo):
            print(combo)
