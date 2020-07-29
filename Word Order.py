# Word Order


from collections import Counter
for i in range(int(input())):
    ctr = Counter(input()) 
print(len(ctr))
print(*ctr.values())
