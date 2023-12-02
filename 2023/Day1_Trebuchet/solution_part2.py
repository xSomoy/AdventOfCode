import re

input_file = open('input.txt', 'r')
Lines = input_file.readlines()


def extract_numbers(text):
    # Define a dictionary to store the mapping of words to numbers
    number_mapping = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
        # Add more mappings as needed
    }

    # Use regular expression to find words representing numbers in the text
    matches = re.findall(
        r'\b(?:' + '|'.join(number_mapping.keys()) + r')\b', text)

    # Convert the matched words to numbers and return them
    numbers = [number_mapping[word] for word in matches]
    print(numbers)
    return numbers


for line in Lines:
    result = extract_numbers(line)
