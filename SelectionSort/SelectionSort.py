def SelectionSort(array):
    for i in range(0, len(array)-1):
        index = FindSmallest(array,i)
        if(index != i):
            temp = array[index]
            array[index] = array[i]
            array[i] = temp
    print(array)

def FindSmallest(array, index):
    smallestIndex = index
    for i in range(index, len(array)):
        if(array[smallestIndex] > array[i]):
            smallestIndex = i
    return smallestIndex

SelectionSort([5,3,4,2,1,4,345,23,0])