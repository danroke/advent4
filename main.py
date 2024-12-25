# regex module
#import re


## input word search is 140x140
cols = 140
rows = 140
word_search_array = [0*cols]*rows # create a 140*140 list object filled with 0's
line_counter = 1
char_counter = 0
# count number of 'XMAS' matches
match_counter = 0

# Read in text
with open('input.txt', 'r') as file:
    for line in file:
        for character in line:
            if character != "\n":   
                word_search_array.insert(char_counter*line_counter, character)
                char_counter += 1
        line_counter += 1

# Look for the next occurance of 'X'
# Check each cardinal direction
char_counter = 0
for character in word_search_array:
    char_counter += 1 
    if character == "X":
        # E
        if word_search_array[char_counter + 1] == "M":
            if word_search_array[char_counter + 2] == "A":
                if word_search_array[char_counter + 3] == "S": 
                    match_counter += 1

    # S
# W
# N

# diagonals
# NE
# SE
# SW
# NW

print(match_counter)
        
        