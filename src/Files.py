# this creates a handle. it doesnt open it, until you call something relevant on the handle which requires a read/write
# file handle is basically a sequence that you can iterate through for lines, or take the whole thing with .read()
handle = open('C:/py/test.txt')
# so this is the contents of the file
contents = handle.read()
print(contents)
print(len(contents), "Characters in the file")

# remember that new line   \n   is a single character in python. so that contents is one string, with a bunch of \n
# that you can't see, but they are there and take up one char in the string

print()
handle = open('C:/py/test.txt')
count = 0

# for loops in python great, they work out how you want to iterate. note it will print a new line twice... if you want
# single \n need to use a diff print function, a bit like print() vs println() in Java

# YOU CAN USE rstrip() TO REMOVE THE TRAILING \n FROM A LINE TO DEAL WITH THIS
for line in handle:
    count += 1
    print(line.rstrip())
    if '2' in line:
        print("The number 2 is in the above line")
print("File contains", count, "lines")

# note at this point, because handle has been used, it will be closed and you can't use handle again, you have to
# reinstantiate
