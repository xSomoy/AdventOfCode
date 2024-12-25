input_file = open('demo_input.txt', 'r')
levels = input_file.readlines()
current_level = []
status = ""
for i in levels:
    j = 0
    current_level = i
    current_level = current_level.split()
    print(len(current_level))
    while j < len(current_level)+1:
        if (abs(int(current_level[j]) - int(current_level[j+1])) <= 2):
            status = "safe"
        else:
            status = "unsafe"
        j += 1
print(status)
