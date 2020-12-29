blah = input('Enter something here to be stored in blah: ')
print(blah)
# input will always give us a string. the below needs to be in a try loop
try:
    blahint = int(blah)
except:
    blahint = -1

print(blahint)


def echo():
    while True:
        echo = input("Enter your word :")
        if echo == "exit":
            break
        print(echo)


echo()
