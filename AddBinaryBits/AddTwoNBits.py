def AddNBits(FirstBinaryArray, SecondBinaryArray):
    carryOut = 0
    size = len(FirstBinaryArray)+1
    addResults = [0]*size
    for i in range(len(FirstBinaryArray)-1,-1,-1):
        addResults[i+1], carryOut = Adder(carryOut,FirstBinaryArray[i],SecondBinaryArray[i])
    if(carryOut):
        addResults[0] = 1
    print(addResults)
    

def Adder(carryIn,FirstValue,SecondValue):
    #one from First Binary array, Second array, and carry out
    carryOut = 0
    arrayResults = 0
    if(FirstValue and SecondValue and carryIn):
        arrayResults = 1
        carryOut = 1
    #one from First Binary array and Second array
    elif(FirstValue and SecondValue):
        arrayResults = 0
        carryOut = 1
    #one from either First or second array but not both and carry out    
    elif(FirstValue or SecondValue and carryIn):
        arrayResults = 0
        carryOut = 1
    #one from only one input(First array, second array, carry out)  
    elif(FirstValue or SecondValue or carryIn):
        arrayResults = 1
        carryOut = 0
    #no one
    else:
        carryOut = 0
    return arrayResults,carryOut


'''
Problem
Input: Two arrays of size N with binary values 
Output: The sum of the two arrays added together 
'''
AddNBits([1,0,0,0,1,1],[1,1,0,0,0,1])