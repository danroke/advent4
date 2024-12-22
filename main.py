# regex module
import re


## input word search is 140x140

with open('input.txt', 'r') as file:
    for line in file:    

        pattern = r"XMAS"
        matches = re.findall(pattern, line)
        
        