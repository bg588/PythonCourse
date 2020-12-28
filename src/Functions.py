def function():
    print("This is a function running!")


def run10times():
    count = 0
    while count < 10:
        print('Execution number ' + str(count))
        function()
        count += 1


print('Hello, running some functions')
function()
run10times()
