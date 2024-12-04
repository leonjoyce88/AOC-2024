import re
input = open('input.txt','r')
input = input.read().replace('\n','')

exp = r"mul\((\d{1,3}),(\d{1,3})\)"


total = sum(int(a)*int(b) for a,b in re.findall(exp,input))
print(total)


exit(0)
def isValidMul(s):
    print(s)
    a = b = ''
    if not s[0].isdigit():
        return 0
    for i in range(3):
        if s[i].isdigit():
            a+=s[i]
        else:
            break
    s = s[len(a):]
    if s[0] != ',':
        return 0
    s = s[1:]
    if not s[0].isdigit():
        return 0
    for i in range(3):
        if s[i].isdigit():
            b+=s[i]
        else:
            break
    s = s[len(b):]
    if s[0] != ')':
        return 0
    print('valid',a,b)

    return int(a)*int(b)





t = 0

while len(input)>4:
    x = input.find('mul(')
    t+= isValidMul(input[x+4:x+20])

    input = input[x+4:]
print(t)
