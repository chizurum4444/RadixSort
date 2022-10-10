from random import randint
from functools import reduce

#function to get value of each digit
def getDigit(num, digit):
    working = num // 10 ** (digit) 
    return working % 10

#returns the length of the largest value in the array
def maxNumOfDigits(array):
    return len(str(max(array)))

def radixSort(array):
    digits = maxNumOfDigits(array)
    for digit in range(0, digits):
        buckets = [[] for i in range(10)]
        for item in array:
            num = int(getDigit(item, digit))
            buckets[num].append(item)

    return buckets

def main():
    array = []
    for i in range(0,10):
        array.append(randint(0,1000000))                                    #generating values that are of 6 digits
    print(array)

    array = reduce(lambda x, y: x + y, radixSort(array))                    #appending the buckets together
    print(array)

main()
