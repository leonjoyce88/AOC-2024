from collections import defaultdict
input = open("input.txt","r")

total = 0
left = []

counts = defaultdict(int)

for line in input:
    a,b = line.split()
    left.append(int(a))
    counts[int(b)] += 1

for num in left:
    total += num * counts[num]

print(total)
