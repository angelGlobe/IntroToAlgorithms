def LinearSearch(array,value):
    for i in range(0,len(array)):
        if(value == array[i]):
            return i;
    return -1


print(LinearSearch([1,3,7,11,13,17],6))
print(LinearSearch([1,3,7,11,13,17],11))

'''
Initialization:
When i=0, the subarray A is empty so there is no values to check 

Iteration:
The body of the for loop works by comparing the current index i to the desired value,
if the value of subarray at i is equal to the desired value then return index i, otherwise
increment i by one to look at the next value in sub array a. 

Termination:
The causing condition of the for loop to terminate is when i is equal to the length of array a. 
This means that all values have been check and none were equal to the desired value. After the code
exist out of the for loop, a return of value -1 is used to inform us that the desired value was not found.
'''