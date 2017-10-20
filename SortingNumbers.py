import random
import numpy

"""
This is a try to implement ascending sort using the hill climbing algorithm.
Of course this is very very inefficient and the number of random swaps needed to completely sort is extremely high.
However, this is a great example of an area where hill climbing can be applied and of the power of randomness to
produce the required solution 

"""



def computeNoOfMisplacedElements(numbers):
    """The function that computes the number of elements that are NOT placed in the ascending fashion."""

    numberNoOfMisplacedElements = 0
    for i in range(0,len(numbers)):
        for j in range(0,len(numbers)-1):
            if numbers[j] > numbers[j + 1]:
                numberNoOfMisplacedElements += 1
    return numberNoOfMisplacedElements










# The global array to be sorted in the ascending order.
array = [4,6,12,3,89,34,65,87,345,8,4,567,34,65]

# Size of the array
sizeOfInput = len(array)

print("Initial Array : ", array)


#   We compute the initial number of misplaced elements, make a random swap and then again compute the final number of
#   misplaced elements. Only if the final value is lesser  than the initial value, we accept the swap, else we revert
#   the swap
counter = 0
while counter < 1000:
    index1 = random.randint(0, sizeOfInput-1)
    index2 = random.randint(0, sizeOfInput-1)
    while index1 == index2:
        index1 = random.randint(0, sizeOfInput - 1)
        index2 = random.randint(0, sizeOfInput - 1)

    initialNoOfMisplacedElements = computeNoOfMisplacedElements(array)

    array[index1], array[index2] = array[index2], array[index1]
    finalNoOfMisplacedElements = computeNoOfMisplacedElements(array)
    if finalNoOfMisplacedElements == 0:
        break
    if initialNoOfMisplacedElements < finalNoOfMisplacedElements:
        array[index1], array[index2] = array[index2], array[index1]

    counter+=1

print("Final sequenced Array : ", array)
