input_file = open('demo_input.txt', 'r')
levels = input_file.readlines()
current_level = []
status = ""
for i in levels:
    current_level = i

for i in current_level:
    j = 0
    k = 1
    data1 = current_level[0]
    data1 = int(data1)
    data2 = current_level[1]
    data2 = int(data2)
    print(type(data2))
