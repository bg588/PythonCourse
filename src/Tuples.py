# a Tuple ("Tupple" like supple) is an immutable list. You can't change the contents. More efficient and performant
# than lists because its a fixed amount of memory...

# this is a 3-tuple
exampletuple = (1, 2, 3)
# this is a 5-tuple
examplefivetuple = ('Dave', 'Steve', 'Harry', 'Pete', 'John')
examplelist = [1, 2, 3]

# to get value from a tuple, works like a list :
print(exampletuple[1])

# cant sort, pop, append etc, limited functionality vs lists

for entry in exampletuple:
    print(entry)

# comparing tuples - checks from left to right, and returns the first condition, stops once it finds something
print((0, 1, 2) < (5, 1, 2))

# sorting dictionaries. useful to be able to sort by key or value - this is sort by value :

c = {'a': 10, 'b': 1, 'c': 22}
# create a temp list
tmp = list()
for k, v in c.items():
    # append value, key tuple to our tmp list
    tmp.append((v, k))

print(tmp)
tmp = sorted(tmp, reverse=True)
print(tmp)
# now can you do whatever on your temp list

# can also use list comprehension - this creates a dynamic list and sorts it
print(sorted([(v, k) for k, v in c.items()]))

a, b = 3, 4
print(b)

# can obviously return tuples etc, lot easier than java!
print((6, 0, 0) > (5, 1, 3))
