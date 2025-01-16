table = {}
lines = open('input.in', 'r').readlines()
for i in lines:
    l, r = i.strip().split(" -> ")
    table[r] = l

print(table['lx'])
