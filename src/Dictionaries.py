# Dictionary is like a HashMap in Java, Key Value pairs. Data structures basically lists and maps, in any language
# Order isnt guaranteed in dictionaries. Think of it as a tiny database. All keys must be unique. Can repeat values
# as many times as you'd like.

# Create an empty dictionary
emptydict = dict()

# Instantiate
treasurechest = {'gold coins': 5, 'silver coins': 10}
print(treasurechest)
print("We have", treasurechest.get('gold coins'), "XAU coins")

numberofcoins = treasurechest.get('gold coins')
print("Add one coin")
numberofcoins += 1

# assign a value to the key
treasurechest['gold coins'] = numberofcoins

print("We now have", treasurechest.get('gold coins'), "XAU coins")

# Also an easier way to increment/update the current value
treasurechest['gold coins'] = treasurechest['gold coins'] + 2
print("We now have", treasurechest.get('gold coins'), "XAU coins")

# Natch can throw errors if you try to get someth that isnt there, so you can get around that with this hack
# this is handy to initialise in a loop
x = treasurechest.get('bronze coins', 0)
print("We have", x, "bronze coins")

# loop through keys
for key in treasurechest:
    print("We have", treasurechest[key], key)

print("Keys are ", treasurechest.keys())
print("Values are", treasurechest.values())
# a list of key value pairs :
print("Items are", treasurechest.items())

# easy way to see keys and values in dictionary, can iterate on two things at same time which is quite unique
for k, v in treasurechest.items():
    print(k, v)

string = "this is a line"
print(string.split()[1])

# Sorting a dictionary using sorted()
d = {'a': 10, 'c': 22, 'b': 1}
print(d.items())
print(sorted(d.items()))
