import re

input_file = open('input.txt', 'r')
Lines = input_file.readlines()


def extract_numbers(text):
    string_number_mapping = {
        'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }
    numbers = ['one', 'two', 'three',
               'four', 'five', 'six', 'seven', 'eight', 'nine',
               '1', '2', '3', '4', '5', '6', '7', '8', '9']
    index = []
    values = []
    for i in numbers:
        if i in text:
            index.append(text.index(i))
            values.append(i)
    unconverted_vals = [values[index.index(min(index))],
                        values[index.index(max(index))]]
    converted_vals = []
    for i in unconverted_vals:
        if len(i) > 1:
            converted_vals.append(string_number_mapping[i])
        else:
            converted_vals.append(int(i))
    final_val = int(str(converted_vals[0]) + str(converted_vals[1]))
    return final_val


all_vals = []
sum = 0
for line in Lines:
    all_vals.append(extract_numbers(line))
for val in all_vals:
    sum = sum + val
    print(val)
# print(extract_numbers('threexfcvbv9qkthree3'))
print(sum)


# Ans: 54925
