table = {}
mem = {}
roots = []
step = {}
lines = open('input.in', 'r').readlines()
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
            mem[key] = ~mem[var]
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
            mem[key] = mem[var1] & mem[var2]
            nextStep(key)


def nextStep(root):
    for i in lines:
        if root in i.split('->')[0].split():
            print(i)
            ops(i)


findRoots()
calcd = roots


def driver():
    for i in roots:
        nextStep(i)


driver()
print(mem)
