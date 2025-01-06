instruction = open('input.txt', 'r').read().strip()
result = instruction.count("(") - instruction.count(")")
print(result)
