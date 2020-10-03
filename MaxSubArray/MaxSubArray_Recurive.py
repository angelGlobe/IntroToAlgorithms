import time 
def FindMaxSubarray(array,low,high):
    if(low == high):
        return low,high,array[low]
    else:
        mid = (low+high)//2
        leftLow,leftHigh,leftSum = FindMaxSubarray(array,low,mid)
        rightLow,rightHigh,rightSum = FindMaxSubarray(array,mid+1,high)
        midLow,midHigh,midSum = CrossMidMax(low,mid,high,array)
        if leftSum > rightSum and leftSum > midSum:
            return leftLow,leftHigh,leftSum
        elif rightSum > leftSum and rightSum > midSum:
            return rightLow,rightHigh,rightSum
        else:
            return midLow,midHigh,midSum

def CrossMidMax(low,mid,high,array):
    leftSum = SmallestNumber
    maxLeftIndex = 0
    sum = 0
    for i in range(mid,low-1,-1):
        sum = sum + array[i]
        if sum > leftSum:
            leftSum = sum
            maxLeftIndex = i
    rightSum = SmallestNumber
    maxRightIndex = 0
    sum = 0
    for i in range(mid+1,high+1):
        sum = sum + array[i]
        if sum > rightSum:
            rightSum = sum
            maxRightIndex = i
    return maxLeftIndex,maxRightIndex,leftSum+rightSum

def FindSmallestNumber(array):
    smallestNumber = array[0]
    for i in range(1,len(array)):
        if smallestNumber > array[i]:
            smallestNumber = array[i]
    return smallestNumber

array = [100,90,70,160,160,169,0,100,23,76,23,43546,34,23,23,6,89,56,12,1231,34,345,6,43245,2,3425,456,24,55467,5467,5768,6879,78,56,45,653,34,5,234,234,2324,54,6245,2345,3256,234,2345,234,523,434,624346,446,12,154,61,57,79,45,34,76,3456,43563,456,765,34,234,2345,5243,2345,342,234,6543,22345,6543,2,3,1324,234,234,234,234,234,2342,32,3423,4234,15]
SmallestNumber = FindSmallestNumber(array) - 1
startTime = time.time()
results = FindMaxSubarray(array,0,len(array)-1)
print("seconds: ",(time.time() - startTime),"Length: ", str(len(array)))
