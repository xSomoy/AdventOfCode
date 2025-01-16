lines = open('input.in', 'r').readlines()
for i in lines:
    if i.split()[0].isnumeric():
        print(i)
