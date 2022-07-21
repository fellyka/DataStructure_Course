import colorama
from colorama import Fore

arrayA = [7, 0, 12, 22, "Book", True] # This a list

try:
    for i in range(len(arrayA)):
        print(Fore.GREEN + f"{arrayA[i + 1]}")
except IndexError:
    print(Fore.RED + 'List value out of range')
