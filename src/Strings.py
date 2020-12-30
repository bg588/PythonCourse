fruit = "banana"

for letter in fruit:
    print(letter)

print('First letter', fruit[0])
print('Second letter', fruit[1])

length = len(fruit)
print('Length is', length)

# prints characters 0 1 2 3 .... note doesn't include final character
print(fruit[0:4])
# just prints character 4
print(fruit[4:5])
# will stop intelligently
print(fruit[5:100])

# boolean condition
print('Contains anan?', 'anan' in fruit)

if 'a' in fruit:
    print('There is an a in fruit')

b = 'b'
c = 'c'
if c > b:
    print('c comes after b')

hi = 'Hi How are you?'
lowercase_hi = hi.lower()
print(lowercase_hi)

print('HI!'.lower())
print('hi'.upper())
print('hi'.capitalize())

# finds the position of the first occurrence of substring
pos = fruit.find('na')
print(pos)
# if it does not find returns -1
pos = fruit.find('zz')
print(pos)

data = 'ben@gmail.com'
atposition = data.find('@')
host = data[atposition + 1: len(data)]
print(host)

# advantage of python 3 is strings are in unicode (ie can represent all character sets, languages etc)
# so don't need to mess arnd with conversion. Python 2 can be more problematic as it isn't as easy
