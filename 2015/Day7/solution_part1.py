table = {}
lines = open('input.in', 'r').readlines()
for i in lines:
    l, r = i.strip().split(" -> ")
    table[r] = l

# print(table['b'])

t = bin(5)[2:].zfill(16)
a = 10
b = 4
print(a >> 1)
