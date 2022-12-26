class qNode():
    def __init__(self):
        self.data = ""
        self.ptr = 0

qLst = [qNode() for i in range(10)]
freeP = 0
StartP = -1

def enQ(item):
    global freeP, StartP
    if freeP == -1:
        print("Overflow... no space availabe.")
    else:
        newP = freeP
        freeP = qLst[freeP].ptr
        qLst[newP].data = item
        qLst[newP].ptr = -1

        if StartP == -1:
            StartP = 0
        else:
            currP = StartP
            preP = -1
            while currP != -1:
                preP = currP
                currP = qLst[currP].ptr
            qLst[preP].ptr = newP

def deQ():
    global StartP, freeP
    if StartP == -1:
        print("Underflow... no value to delete.")
        return "@"
    else:
        theP = freeP
        item = qLst[StartP].data
        freeP = StartP
        StartP = qLst[StartP].ptr
        qLst[freeP].ptr = theP
        return item

def options():
    print("1. Add Q")
    print("2. Delete from Q")
    print("3. Print Q")
    print("4. Inroder Traversal")
    print("5. Quit")
    x = int(input("Enter option... "))
    return x

def printQ():
    print("StartP:", StartP, "\t FreeP: ", freeP)
    for i in range(10):
        print(i, qLst[i].data, qLst[i].ptr, sep="\t")

def printInOrder():
    currP = StartP
    while currP != -1:
        print(qLst[currP].data)
        currP = qLst[currP].ptr

def initQ():
    global freeP, StartP
    freeP = 0
    StartP = -1

    for i in range(10):
        qLst[i].data = ""
        qLst[i].ptr = i+1
    qLst[9].ptr = -1

# main program
initQ()
x = options()
while x != 5:
    if x == 1:
        item = input("Enter value to Enqueue: ")
        enQ(item)
    elif x == 2:
        item = deQ()
        if item != "@":
            print("Item de queued: ", item)
    elif x == 3:
        printQ()
    else:
        printInOrder()
    x = options()