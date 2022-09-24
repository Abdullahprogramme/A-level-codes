# Write your code here :-)
#insert sort algorithim:
Flag = True
array=[2,7,9,3,5]
def Insertsort():
    for cn in range(1,len(array)):
        temp= array[cn]
        pointer= cn - 1
        while array[pointer] > temp and  pointer > -1:
            array[pointer + 1] = array[pointer]
            pointer = pointer - 1
        array[pointer + 1] = temp
Insertsort()
print(array)

def anotherInsertSort():
    for blackP in range(1,len(array)):
        for blueP in range(0,blackP - 1):
            if array[blackP] < array[blueP]:
                temp = array[blackP]
                for i in range(blackP,blueP +1, -1):
                    array[i ] = array[i-1]
                array[blueP] = temp
                break

anotherInsertSort()
print(array)
