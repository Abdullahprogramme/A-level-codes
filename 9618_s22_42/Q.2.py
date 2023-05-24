import random as r

def output():
    for rows in range(10):
        for columns in range(10):
            print(array[rows][columns], "  ",  end = '')
        print('')    

array = [[0 for i in range(10)] for j in range(10)] #Integer
for i in range(10):
    for j in range(10):
        array[i][j] = r.randint(1, 100)
print("Array before")    
output()

ArrayLength = 10
for x in range(0, ArrayLength - 1):
    for y in range(0, ArrayLength - 2):
        for z in range(0, ArrayLength - y - 2):
            if array[x][z] > array[x][z + 1]:
                TempValue = array[x][z]
                array[x][z] = array[x][z + 1]
                array[x][z + 1] = TempValue
print("Array after")  
output()

def BinarySearch(SearchArray, Lower, Upper , SearchValue):
    if Upper >= Lower:
        Mid = (Lower + (Upper - 1)) // 2
        if SearchArray[0][Mid] == SearchValue:
            return Mid
        else:
            if SearchArray[0][Mid] > SearchValue:
                return BinarySearch(SearchArray, Lower, Mid - 1, SearchValue)
            elif SearchArray[0][Mid] < SearchValue:
                return BinarySearch(SearchArray, Mid + 1, Upper, SearchValue)
    return -1

answer = int(input('enter a value to search: '))
returnvalue = BinarySearch(array, 0, 10, answer)
if returnvalue == -1:
    print('Value not found')
else:
    print('Value found')
    answer = int(input('enter a value to search: '))
returnvalue = BinarySearch(array, 0, 10, answer)
if returnvalue == -1:
    print('Value not found')
else:
    print('Value found')