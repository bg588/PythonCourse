entry = input("Please enter a number ")
# this will fail if entry is not an int
# entry = int(entry)

# so we need to do exception handling
try:
    entry = int(entry)
except:
    print("Exception - you need to enter a number")
    entry = -1
# this will still run!
print(entry)
