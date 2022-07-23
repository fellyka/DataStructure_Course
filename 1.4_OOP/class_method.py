### The class method can also be called directly through
### the class object without instantiating the class. A class method is defined
### using the @classmethoddecorator

from colorama import Fore

class book:
    price = 100
    @classmethod
    def display(cls):
        print(cls.price)
    @staticmethod
    def printSomething():
        name = 'FellyKa...'
        print(f"This name, from the static method is, {name}")
    def show(self, x):
        self.price = x
        print(self.price)

try:
    b = book()
    c = book()
    # The display() method is called here with the class rather than with the object
    print('The display method printed by the class name:')
    book.display()
    print('\n')

    # Calling the display() method with the object b
    print('The display method printed by the b object:')
    b.display()
    print('\n')

    # The show() method can only be called by the instantiated object
    print('The show method printed by the b and c  objects respectively: ')
    b.show(200)
    c.show(700)
    print('\n')

    # The static method printSomething printed by its class
    print('The printSomething() static method printed by the book class: ')
    book.printSomething()

    print('\n')

    print('The printSomething() static method printed by the b object:')
    b.printSomething()
    print('\n')

    # The show() method won't be printed because it is neither a class nor a static method.
    # It raises an error that is handled below
    book.show()

except :
    print(Fore.RED + "book.show() method raised an error")


