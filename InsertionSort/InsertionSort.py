#Ascending Order
def InsertSort(unsortedArray):
    #key assignment 
    for j in range(0,len(unsortedArray)):
        key = unsortedArray[j]
        i =  j -1
        while i >= 0 and unsortedArray[i] > key:
            unsortedArray[i+1] = unsortedArray[i]
            i = i -1 
        unsortedArray[i+1] = key
                
    print(unsortedArray)
InsertSort([3,2,1,2,3])