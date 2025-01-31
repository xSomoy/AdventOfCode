table = {}
mem = {}
roots = []
step = {}
lines = open('input.in', 'r').readlines()
# lines = open('demo.in', 'r').readlines()
for i in lines:
    l, r = i.strip().split(" -> ")
    table[r] = l
    step[i] = r


def findRoots():
    for i in table:
        if table[i].isdigit():
            mem[i] = table[i]
            roots.append(i)


def ops(cmd):
    if cmd.startswith("NOT"):
        var = cmd.split()[1]
        key = cmd.split()[-1]
        if var in calcd:
            var1 = bin(int(mem[var]))[2:].zfill(16)
            var2 = ''.join('1' if c == '0' else '0' for c in var1)
            var = int('0b' + var2, 2)
            mem[key] = var
            nextStep(key)

    if "LSHIFT" in cmd.split():
        var1 = cmd.split()[0]
        var2 = cmd.split()[2]
        key = cmd.split()[-1]
        if var1 in mem:
            var1 = int(mem[var1])
            var2 = int(var2)
            mem[key] = var1 << var2
            nextStep(key)

    if "RSHIFT" in cmd.split():
        var1 = cmd.split()[0]
        var2 = cmd.split()[2]
        key = cmd.split()[-1]
        if var1 in mem:
            var1 = int(mem[var1])
            var2 = int(var2)
            mem[key] = var1 >> var2
            nextStep(key)

    if "AND" in cmd.split():
        var1 = cmd.split()[0]
        var2 = cmd.split()[2]
        key = cmd.split()[-1]
        if var1 in calcd and var2 in calcd:
            print(var1, var2)
            var1 = int(mem[var1])
            var2 = int(mem[var2])
            mem[key] = var1 & var2
            nextStep(key)
        else:
            newStep(var1, var2)

    if "OR" in cmd.split():
        var1 = cmd.split()[0]
        var2 = cmd.split()[2]
        key = cmd.split()[-1]
        if var1 in calcd and var2 in calcd:
            var1 = int(mem[var1])
            var2 = int(mem[var2])
            mem[key] = var1 | var2
            nextStep(key)
        newStep(var1, var2)


def newStep(var1, var2):
    if var1 not in mem:
        nextStep(var1)
    else:
        nextStep(var2)


def nextStep(root):
    for i in lines:
        if root in i.split('->')[0].split():
            print(i)
            ops(i)


findRoots()
calcd = roots


# def driver():
# for i in roots:
#     nextStep(i)


# driver()
# driver()
nextStep('s')
# print(table['s'])
print(mem)
