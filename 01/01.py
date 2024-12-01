input = open("input.txt","r")

total = 0
left = []
right = []

for line in input:
    a,b = line.split()
    left.append(a)
    right.append(b)

left= sorted(left)
right= sorted(right)

for (a,b) in zip(left,right):
    total += abs(int(a)-int(b))

print(total)
