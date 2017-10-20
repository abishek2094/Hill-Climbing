import random

"""
Given an array of the form = [a0, a1, a2, a3, a4, a5,..., an-1], we sequence the elements such that we obtain the following sequence,

[a0 < a1 > a2 < a3 > a4 < a5 ....].

I have chosen to solve this problem using the method of Hill Climbing.

"""



def computeNoOfMisplacedElements(numbers):
    """The function that computes the number of elements that are NOT placed in the required manner."""

    numberNoOfMisplacedElements = 0
    for i in range(0,len(numbers)-1):
        if i % 2 ==0:
            if numbers[i] > numbers[i+1]:
                numberNoOfMisplacedElements += 1
        else:
            if numbers[i] < numbers[i + 1]:
                numberNoOfMisplacedElements += 1
    return numberNoOfMisplacedElements










# The global array to be sequenced in the required fashion.
array = [1,2,3,4,5,5,5,5,5,5,5,5,7]

#Size of the array
sizeOfInput = len(array)

print("Initial Array : ", array)


#   We compute the initial number of misplaced elements, make a random swap and then again compute the final number of
#   misplaced elements. Only if the final value is lesser  than the initial value, we accept the swap, else we revert
#   the swap
counter = 0
while counter < (sizeOfInput*sizeOfInput):
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
