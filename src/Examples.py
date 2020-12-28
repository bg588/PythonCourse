x = 1
y = 2
z = 3
print(x)
print(x, y, z)

mylistofnumbers = x, y, z

print(mylistofnumbers)

for blah in mylistofnumbers:
    print(blah)

for blah in mylistofnumbers:
    if blah < 2:
        print("Number is 1 : ")
        print(blah)
    if blah == 2:
        print("Number is 2 : ")
        print(blah)
    if blah > 2:
        print("Number is 3 : ")
        print(blah)
