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

array = [100,90,70,160,160,169,0,100]
displayMessge = "Start Index {0} End Index {1} Max Sum {2}"
print(MaxSubArray(array))