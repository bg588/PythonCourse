# need to import the regex library
import re

# simple search :
x = 'Hello how are you?'
if re.search('how', x):
    print('found')

# find all numbers. findall will return a list. it will also return an empty list if no occurence.
# + is 1 or more, * is 0 or more. [0-9] means 1 char between 0 and 9. [a-d] means one char between a and d etc.
# ^ starts with

x = 'My 2 favourite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
print(y)

