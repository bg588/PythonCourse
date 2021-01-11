# need to import the regex library
import re

# simple search :
x = 'Hello how are you?'
if re.search('how', x):
    print('found')

# find all numbers. findall will return a list. it will also return an empty list if no occurence.
# + is 1 or more, * is 0 or more. [0-9] means 1 char between 0 and 9. [a-z] means one char between a and z etc.
# ^ starts with. \S non blank


x = 'My 2 favourite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
print(y)

# by default it is greedy matching. tries to return the very biggest string it can from the search string.
# add ? to stop as soon as you achieve

x = 'from dave@test.com blah blah 12 blah'
# this will return the whole email address
y = re.findall('\S+@\S+', x)
print(y)
# if we make it non greedy, we get dave@t.... ie as soon as it has achieved goal it stops printing. be careful with this
y = re.findall('\S+@\S+?', x)
print(y)

# you can specify search term as longer than what you extract, using () eg
y = re.findall('from (\S+@\S+)', x)
print(y)

# if you want to search for a special char, eg you want to find *, you need to put a \ before it.... ie '\*'
# to search for *

