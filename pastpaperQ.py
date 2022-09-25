freeNode = 0
null = -1
root = null
ArrayNodes= [ [null for columns in range(3)] for rows in range(20)]
#print(ArrayNodes)

def AddNode():
    global root, freeNode
    print("Enter the value you want to enter: ")
    answer = int(input("enter value : "))
    if freeNode <= 19:
        ArrayNodes[freeNode][0] = -1
        ArrayNodes[freeNode][1] = answer
        ArrayNodes[freeNode][2] = -1
        if root == -1:
            root = 0
        else:
            placed = False
            currentNode= root
            while placed == False:
                if answer < ArrayNodes[currentNode][1]:
                    if ArrayNodes[currentNode][0] == null:
                        ArrayNodes[currentNode][0] = freeNode
                        placed = True
                    else:
                        currentNode = ArrayNodes[currentNode][0]
                elif answer > ArrayNodes[currentNode][1]:
                    if ArrayNodes[currentNode][2] == null:
                        ArrayNodes[currentNode][2] = freeNode
                        placed =True
                    else:
                        currentNode = ArrayNodes[currentNode][2]
        freeNode = freeNode + 1
    else:
        print("Tree is full")
for i in range(20):
    AddNode()

x = 0

def PrintAll():
    global x
    print("    LeftPointer ","  Data  " , " RightPointer " )
    for i in ArrayNodes:
        a = i[0]
        b = i[1]
        c = i[2]
        print(x,"    " , a, "           ",b , "           " , c)
        x += 1

print("#Printing all nodes ")
PrintAll()

def Traversal(root):
    if root!= null:
        Traversal(ArrayNodes[root][0])
        print(ArrayNodes[root][1])
        Traversal(ArrayNodes[root][2])

print("#InOrder Traversal ")
Traversal(root)
