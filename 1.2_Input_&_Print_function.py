# This simple program teaches how to use the input and the print functions respectively
# Enter 2 Values then retrieve them and print them


inValue = input('Enter a and b. separate them by a coma: ')
actualValue = inValue.split(',')
a = int(actualValue[0])
b = int(actualValue[1])

print(f"Values entered were a = {a} and b = {b}")
