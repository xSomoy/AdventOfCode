input_file = open('input.txt', 'r')
Lines = input_file.readlines()
num = []
values = []
sum = 0
for line in Lines:
    for i in line:
        if i.isdigit():
            num.append(i)
    num2 = str(num[0]) + str(num[-1])
    values.append(int(num2))
    num = []
for val in values:
    sum += val
print(sum)
