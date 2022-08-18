def divide(a,b):
    return a/b 
a,b=input("Enter 2 number: ").split()
a=int(a)
b=int(b)

try:
    divide(a,b)
except ZeroDivisionError as err:
    print('Handling run-time error:', err)