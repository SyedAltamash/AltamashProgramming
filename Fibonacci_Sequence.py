#from math import e
#result = input('How many decimal places do you want to print for e: ')
#print('{:.{}f}'.format(e, result))
def fibonacci_sequence(number):
    list = []
    a =1
    b = 1
    for i in range(number):
        list.append(a)
        a,b = b,a+b
    print(list)


result = int(input('Hey enter a number for the Fibonacci Sequence: '))
fibonacci_sequence(result)