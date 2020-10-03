import time
def MaxSubArray(array):
    low = 0
    high = 0
    maxSum = 0
    for i in range(len(array)):
        startingPrice = array[i]
        currentProfit = 0
        greatestProfit = 0
        maxSum  = array[i]
        for j in range(i+1,len(array)):
            currentProfit = array[j] - startingPrice
            if(currentProfit > greatestProfit):
                greatestProfit = currentProfit
                high = j 
        if(greatestProfit > maxSum):
            maxSum =  greatestProfit
            low = i
    return low,high,maxSum

array = [100,90,70,160,160,169,0,100,23,76,23,43546,34,23,23,6,89,56,12,1231,34,345,6,43245,2,3425,456,24,55467,5467,5768,6879,78,56,45,653,34,5,234,234,2324,54,6245,2345,3256,234,2345,234,523,434,624346,446,12,154,61,57,79,45,34,76,3456,43563,456,765,34,234,2345,5243,2345,342,234,6543,22345,6543,2,3,1324,234,234,234,234,234,2342,32,3423,4234,15]
displayMessge = "Start Index {0} End Index {1} Max Sum {2}"
startTime = time.time()
results = MaxSubArray(array)
print("seconds: ",(time.time() - startTime),"Length: ", str(len(array)))