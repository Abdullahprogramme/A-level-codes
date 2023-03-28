class Tree():
    def __init__(self, lft, dat, rgt):
        self.left = lft
        self.data = dat
        self.right = rgt

ArrayNodes = [Tree(-1, -1, -1) for j in range(20)]

ArrayNodes[0] = Tree(1, 20, 5)
ArrayNodes[1] = Tree(2, 15, -1)
ArrayNodes[2] = Tree(-1, 3, 3)
ArrayNodes[3] = Tree(-1, 9, 4)
ArrayNodes[4] = Tree(-1 , 10, -1)
ArrayNodes[5] = Tree(-1, 58, -1)
ArrayNodes[6] = Tree(-1, -1, -1)
FreeNode = 6
RootPointer = 0

def SearchValue(Root, ValueToFind):
    global ArrayNodes
    if Root == -1:
        return -1
    else:
        if ArrayNodes[Root][1] == ValueToFind:
            return Root
        elif ArrayNodes[Root][1] == -1 :
            return -1 
    if ArrayNodes[Root][1] > ValueToFind:
        return SearchValue(ArrayNodes[Root][0], ValueToFind)
    if ArrayNodes[Root][1] < ValueToFind:
        return SearchValue(ArrayNodes[Root][2], ValueToFind)
    
def PostOrder(Root):
    if Root[0] != -1:
        PostOrder(ArrayNodes[Root[0]])
    if Root[2] != -1:
        PostOrder(ArrayNodes[Root[2]])
    print(ArrayNodes[Root][1])

answer = SearchValue(RootPointer,15)
if answer == -1:
    print("Value not found")
else:
    print("Value found at: ", str(answer))
PostOrder(ArrayNodes[RootPointer])