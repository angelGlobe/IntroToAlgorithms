def MergeSort(array,start,end):
    if(start<end):
        halfPoint = (end + start)//2
        MergeSort(array,start,halfPoint)
        MergeSort(array,halfPoint+1,end)
        Merge(array,start,halfPoint,end)
    print(array)

def Merge(array,start,halfPoint,end):
    leftSize = halfPoint-start+1
    rightSize = end-halfPoint
    leftArray = [0]*(leftSize)
    rightArray = [0]*(rightSize)

    
    for i in range(0,leftSize):
        leftArray[i] = array[start+i]
    for i in range(0,rightSize):
        rightArray[i] = array[halfPoint+i+1]


    indexL = 0
    indexR = 0
    for k in range(start,end+1):
        if(indexL == leftSize):
            array[k] = rightArray[indexR]
            indexR+=1
        elif(indexR == rightSize):
            array[k] = leftArray[indexL]
            indexL+=1
        elif(leftArray[indexL] <= rightArray[indexR]):
            array[k] = leftArray[indexL]
            indexL+=1
        else:
            array[k] = rightArray[indexR]
            indexR+=1
            
array=[0,1,2,3,2,1,0]
arraySize = len(array)-1
MergeSort(array,0,arraySize)

