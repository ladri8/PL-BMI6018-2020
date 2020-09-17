from os import getcwd
from prime.primeFuncs import isPrime

print('this is the cwd:', getcwd())

if __name__ == "__main__":

    s = input('Enter a comma seperated list of integers: ')

    intList = []
    for i in s.split(','):
        i = int(i)
        intList.append(i)

    for i in intList:
        print(i, isPrime(i))
