import re

file_path = 'puzzleinput.txt'

calibrated_numbers_array = []
total_count = 0

with open(file_path, 'r') as file:
    for line in file:
        first_number = re.search("[1-9]", line)
        last_number = re.search("(\d+)(?!.*\d)", line)
        finalNumber = first_number.group() + last_number.group()
        convertedFinalNumber = int(finalNumber)
        print("this is the line: ", line,  " this is the converted final number:", convertedFinalNumber)
        total_count += convertedFinalNumber
        calibrated_numbers_array.append(finalNumber)

print(total_count)