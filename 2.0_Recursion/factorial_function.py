# If n! = 0, the function returns 1
# If n >= 1, the function returns n * (n-1)!

# define Python user-defined exceptions

class Error(Exception):
    """Base class for other exceptions"""
    pass


class NegativeValue(Error):
    """Base class for negative exceptions"""
    pass


try:
    def factorial(n):
        if n < 0:
            raise NegativeValue
        elif n==0:
            return 1
        else :
            value = n * factorial(n-1)
            return value

except NegativeValue:
    print("Value cannot be negative")

n = int(input("Enter a positive number to find its factorial value:"))
x = factorial(n)
print(f"Factorial of {n} is {x}")



