input_file = open('demo_input.txt', 'r')
Lines = input_file.readlines()
for i in Lines:
    print(i.split()[0])
print("\n")
for i in Lines:
    print(i.split()[1])
