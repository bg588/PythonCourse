def testFunction():
    print("This is a function running!")

def run10Times():
    count = 0
    while count < 10 :
        print('Execution number ' + str(count))
        testFunction()
        count += 1

print('Hello, running some functions')
testFunction()
run10Times()

