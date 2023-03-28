DataArray =[ 0 for i in range(100)]

def ReadFile():
    global i
    try:
        with open('IntegerData.txt') as f:
            for i in range(100):
                number =  f.readline().strip() 
                DataArray[i] = int(number)
        f.close()        
    except:
        print('File not found')

def FindValues():
    global DataArray
    Counter = 0

    value = int(input("Enter a whole number between 1 and 100: "))
    if value < 1 or value > 100:
        while value < 1 or value > 100 :
            value = int(input("Enter a whole number between 1 and 100: "))

    for i in range(100):
        if DataArray[i] == value :
            Counter = Counter + 1

    return Counter
#MAIN
ReadFile()
print(DataArray)
answer = FindValues()
print('The number was found : ', str(answer), ' times')

def BubbleSort():
    global DataArray
    Swaps = False
    items = len(DataArray)
    while Swaps == False:
        Swaps = True
        for i in range(items - 1):
            if DataArray[i] > DataArray[i + 1]:
                Swaps = False
                temp = DataArray[i]
                DataArray[i] = DataArray[i + 1]
                DataArray[i + 1] = temp
        items -= 1

BubbleSort()
print(DataArray)