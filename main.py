# regex module
#import re


## input word search is 140x140
cols = 140
rows = 140
word_search_array = [0*cols]*rows # create a 140*140 list object filled with 0's
line_counter = 1
char_counter = 0

print(word_search_array)

with open('input.txt', 'r') as file:
    for line in file:
        for character in line:   
            word_search_array.insert(char_counter*line_counter, character)
            char_counter += 1
        line_counter += 1
print(word_search_array)
        
        