def function():
    print("This is a function running!")


def run10times():
    count = 0
    while count < 10:
        print('Execution number ' + str(count))
        function()
        count += 1


def breaktest():
    x = 0
    while x < 10:
        x += 1
        if x == 2:
            # continue causes us to go back to top of loop, so 2 won't print out
            continue
        print(x)
        if x == 7:
            # break causes us to leave the while totally
            break
    print("Now here as we left the loop at ", x)


def countdown():
    n = 5
    while n > 0:
        print(n)
        n -= 1
    print('Blast off!')


def givemeab():
    # note lack of type - not like java
    return "B"


print("Give me a B!", givemeab())
print()
print("Break test : ")
breaktest()
print()
print('Hello, running some functions')
function()
run10times()
print('Launch a rocket')
countdown()
print('Stopping here')
exit()
print('This will not run')
