queueData = ['' for i in range(20)]
StartPointer = 0
EndPointer = 0

def Enqueue(value):
    global  EndPointer
    max = 20
    if EndPointer == max:
        print("queue is full")
        return False
    else:
        queueData[EndPointer] = value
        EndPointer += 1
        return True
    
def ReadFile():
    filename = input('Enter a filename: ')
    try:
        file = open(filename, 'r')
        line = file.readline().strip()
        answer = True
        while answer == True and line != "":
            answer = Enqueue(line)
            line = file.readline().strip()
        if answer is False:
            file.close()
            return 1
        else:
            file.close()
            return 2
    except:
        return -1
    
returnvalue = ReadFile()
if returnvalue == -1:
    print("File could not be found")
elif returnvalue == 1:
    print("Queue was full, all data was not read")
elif returnvalue == 2:
    print ("All data read successfully")

def Remove():
    global StartPointer
    max = 20
    if StartPointer == max:
        print("Queue iss empty")
    else:
        if EndPointer - StartPointer < 2:
            return "NoItems"
        else:
            value1 = queueData[StartPointer]
            StartPointer += 1
            value2 = queueData[StartPointer]
            StartPointer += 1
            return(value1 +" " + value2)