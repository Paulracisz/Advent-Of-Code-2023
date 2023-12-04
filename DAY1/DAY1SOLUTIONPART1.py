# PART 1

# import regex
import re

# import the input file
file_path = 'puzzleinput.txt'

# total count of digit numbers
total_count = 0

# open the file, read only
with open(file_path, 'r') as file:
    # iterate over each line in the file
    for line in file:
        # regex group that captures the first digit in a given string
        first_number = re.search("\d", line)
        # regex group that captures the last digit in a given string
        last_number = re.search("(\d+)(?!.*\d)", line)
        # last_number can sometimes double up, so if string is greater than 1, grab the last digit in string
        if len(last_number.group()) > 1:
            # slice last digit off to avoid duplicate numbers
            last_number = last_number.group()[-1]
            # put two digits together ex: ("4" and "5" becomes "45")
            finalNumber = first_number.group() + last_number
        else:
        # is the last_number is not doubled up, just add the groups (str values) together
            finalNumber = first_number.group() + last_number.group()
        # convert it into an int for adding to the final number
        convertedFinalNumber = int(finalNumber)
        # add them all together
        total_count += convertedFinalNumber

# print the total count to find the answer
print(total_count)