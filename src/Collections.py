numbers = [5, 4, 3, 2, 1]
for blah in numbers:
    print(blah)

# square brackets is a list
names = ['Ben', 'James', 'Chris', 'Dave']
for name in names:
    print(name)

# can have empty lists or lists within lists obviously
emptylist = list()

numbers = [1, [2, 3]]
for entry in numbers:
    print(entry)

print("Entry at index 1", numbers[1])

print("Length of names list:", len(names))

# use range to get behaviour equivalent to java for loops
# range generates a list of length in range. eg range(3) gives range(0,3), list(range(3)) gives [0,1,2]
for i in range(len(names)):
    print(names[i])

x = range(4)
y = list(range(4))
print(x)
print(y)

# if you add lists you concatenate them
totallist = names + numbers
print(totallist)

# lists can be sliced like a string
# from 2nd entry onwards
print(names[2:])
# print last three entries
print(totallist[len(totallist)-3:])

# can append to list
names.append('Steve')
print(names)
# note that totallist isnt updated... this is a 'different' names
print(totallist)

# boolean to check whether item in list
print('Steve' in names)

# append adds at end, if you want to add somewhere else, use insert, with the position you want to insert at
names.insert(3, 'Benji')
print(names)

# call sort to sort list
names.sort()
print("Sorted:", names)

# easy to work with numbers as well - built in functions in python take lists as parameters

nums = [1, 2, 5, 25]
print("Nums array :", nums)
print("Length is :", len(nums))
print("Max is :", max(nums))
print("Min is :", min(nums))
print("Sum is :", sum(nums))
print("Average is :", sum(nums)/len(nums))

# can make a sentence into a list easily, use split() to split on spaces. Number of spaces doesn't matter
sentence = 'This is a sentence'
listofwords = sentence.split()
print(listofwords)

# can use diff delimiters also
diffdelimiter = 'Dave;Pete;Paul'
listofwords = diffdelimiter.split(';')
print(listofwords)
