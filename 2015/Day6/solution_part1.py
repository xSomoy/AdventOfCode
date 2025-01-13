lines = open('input.txt', 'r').readlines()
# lights[999, 999] = {0}
for i in lines:
    print(i.split()[0])
    print(i.split()[1].split(","))
