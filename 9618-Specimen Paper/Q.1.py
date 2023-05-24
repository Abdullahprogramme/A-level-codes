TheData = [20, 3, 4, 8, 12, 99, 4, 26, 4]

def Insertionsort(TheData):
    for Count in range(len(TheData)):
        DataToInsert = TheData[Count]
        NextValue = Count - 1
        Inserted = 0
        while NextValue > -1 and Inserted != 1:
            if DataToInsert < TheData[NextValue]:
                TheData[NextValue + 1] = TheData[NextValue]
                NextValue -= 1
                TheData[NextValue + 1] = DataToInsert
            else: Inserted = 1
def OutputAll(TheData):
    for i in range(len(TheData)):
        print(TheData[i])
    
print("Before")
OutputAll(TheData)
Insertionsort(TheData)
print("After")
OutputAll(TheData)

def search(TheData):
    Found = False
    number = int(input("Enter a number to search: "))
    for i  in range(len(TheData)):
        if TheData[i] == number :
            Found = True
            break
        else:
            Found = False
    if Found is True:
        print('found')
        return True
    else:
        print('not found')
        return False

answer = search(TheData)
if answer == True:
    print('found')
else: print('not found')

answer = search(TheData)
if answer == True:
    print('found')
else: print('not found')