#global variables
NULLPOINTER = -1
CurrentNodePtr = TopOfStack = FreeListPtr = 0
Stack = []

class Node:
    def __init__(self, Data, Pointer):
        self.Data = Data
        self.Pointer = Pointer

def InitialiseStack():
    global TopOfStack, FreeListPtr
    TopOfStack = NULLPOINTER
    FreeListPtr = 0
    for Index in range(8):
        Stack.append(Node("", Index + 1))
    Stack[7].Pointer = NULLPOINTER

def Push(NewItem):
    global TopOfStack, FreeListPtr
    if FreeListPtr != NULLPOINTER:
        NewNodePtr = FreeListPtr
        Stack[NewNodePtr].Data = NewItem
        FreeListPtr = Stack[FreeListPtr].Pointer
        Stack[NewNodePtr].Pointer = TopOfStack
        TopOfStack = NewNodePtr
    else:
        print("no space for more data")

def Pop():
    global TopOfStack, FreeListPtr
    if TopOfStack == NULLPOINTER:
        print("no data on stack")
        Value = ""
    else:
        Value = Stack[TopOfStack].Data
        ThisNodePtr = TopOfStack
        TopOfStack = Stack[TopOfStack].Pointer
        Stack[ThisNodePtr].Pointer = FreeListPtr
        FreeListPtr = ThisNodePtr
    return Value

def OutputAllNodes():
    global TopOfStack, FreeListPtr
    CurrentNodePtr = TopOfStack
    if TopOfStack == NULLPOINTER:
        print("no data on stack")
    while CurrentNodePtr != NULLPOINTER:
        print(CurrentNodePtr, Stack[CurrentNodePtr].Data)
        CurrentNodePtr = Stack[CurrentNodePtr].Pointer
    print(CurrentNodePtr, Stack[CurrentNodePtr].Data)

def GetOption():
    print("1: Push a value\n2: Pop a value\n3: Output Stack\n4: End Program")
    choice = int(input("Enter your choice: "))
    return choice

InitialiseStack()
Choice = GetOption()
while Choice != 4:
    if Choice == 1:
        Data = input("Enter the value: ")
        Push(Data)
        OutputAllNodes()
    if Choice == 2:
        Data = Pop()
        print("Data popped:", Data)
    if Choice == 3:
        OutputAllNodes()
        print("\n\n")
        print("TopOfStack:",TopOfStack, "FreeListPtr:",FreeListPtr)
        for i in range(8):
            print(i, Stack[i].Data, Stack[i].Pointer)
    Choice = GetOption()