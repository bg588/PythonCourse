def function():
    print("This is a function running!")


def run10times():
    count = 0
    while count < 10:
        print('Execution number ' + str(count))
        function()
        count += 1


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

print('Hello, running some functions')
function()
run10times()
print('Launch a rocket')
countdown()
print('Stopping here')
exit()
print('This will not run')
