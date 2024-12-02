input = open("input.txt","r")

def isSafe(line):
    diff = [x-y for x,y in zip(line,line[1:])]
    return all(1<=x<=3 for x in diff) or all(-1>=x>=-3 for x in diff)

total =0
for line in input:
    line = [int(c) for c in line.split()]
    if any(isSafe(line[:i]+line[i+1:]) for i in range(len(line))):
        total+=1
print(total)






