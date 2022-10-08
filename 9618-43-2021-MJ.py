class node():
    def __init__(self):
        self.data = 0
        self.nextNode = 0

LinkedList = [node() for i in range(10)]
Null = -1
startPointer = 0
freeP = 0
def initialize():
    global startPointer,  freeP
    LinkedList[0].data = 1
    LinkedList[0].nextNode = 1
    LinkedList[1].data = 5
    LinkedList[1].nextNode = 4
    LinkedList[2].data = 6
    LinkedList[2].nextNode = 7
    LinkedList[3].data = 7
    LinkedList[3].nextNode = -1
    LinkedList[4].data = 2
    LinkedList[4].nextNode = 2
    LinkedList[5].data = 0
    LinkedList[5].nextNode = 6
    LinkedList[6].data = 0
    LinkedList[6].nextNode = 8
    LinkedList[7].data = 56
    LinkedList[7].nextNode = 3
    LinkedList[8].data = 0
    LinkedList[8].nextNode = 9
    LinkedList[9].data = 0
    LinkedList[9].nextNode = -1
    startPointer = Null
    freeP = 5
def OutputNode(startp):
    while startp != -1:
        print(LinkedList[startp].data, "   ", LinkedList[startp].nextNode)
        startp = LinkedList[startp].nextNode

initialize()
OutputNode(0)
print("############")
print("############")
def addNode(Val):
    global freeP , Null, startPointer
    if freeP != Null:
        NewNode = freeP
        LinkedList[NewNode].data = Val
        freeP = LinkedList[freeP].nextNode
        pp = Null
        cn = startPointer
        while cn!= Null and LinkedList[cn].data < Val:
            pp = cn
            cn = LinkedList[cn].nextNode
        if pp == Null:
            LinkedList[NewNode].nextNode = startPointer
            startPointer = NewNode
        else:
            LinkedList[pp].nextNode = NewNode
            LinkedList[NewNode].nextNode = cn
    else:
        print("LinkedList full")
addNode(5)
print("Pointer    data      pointer")
for i in range(10):
    print(i , "            " , LinkedList[i].data , "           " , LinkedList[i].nextNode)