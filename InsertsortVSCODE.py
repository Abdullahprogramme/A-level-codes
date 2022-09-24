#Insert sort algorithim
array= [2,9,4,0,6,8,5]
def Insertsort():
    for cn in range(1,len(array)):
        temp = array[cn]
        pointer = cn - 1
        while array[pointer] > temp and pointer > -1:
            array[pointer + 1] = array[pointer]
            pointer -= 1
        array[pointer + 1] = temp

Insertsort()
print(array)