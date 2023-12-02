import re

input_file = open('input.txt', 'r')
Lines = input_file.readlines()


def extract_numbers(text):
    # Define a dictionary to store the mapping of words to numbers
    number_mapping = ['zero', 'one', 'two', 'three',
                      'four', 'five', 'six', 'seven', 'eight', 'nine',
                      '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    # Use regular expression to find words representing numbers in the text
    value = []
    for i in number_mapping:
        if i in text:
            value.append(text.index(i))

        # print(i)
    return value


print(extract_numbers('two2seven7'))
# for line in Lines:
#     result = extract_numbers(line)
