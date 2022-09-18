def initiliaze():
    stac=[]
    for i in range(9):
        stac[i]=0

stac=[0,0,0,0,0,0,0,0,0]
Top = -1
Max = 8
def push(Val):
    global Max,Top
    if Top==Max:
        print("Overflow occurred")
    else:
        Top = Top + 1
        stac[Top]=Val
        print(Val,"added")


def pop():

    global Max, Top
    removed=0
    if Top==0:
        print("underflow occurred")
    else:
        removed=stac[Top]
        print(stac[Top], "removed")
        Top = Top - 1
    return removed

def showStack():
    for i in range(8,-1,-1):
        print(i,"  " , stac[i])

def getoption():
    print("Type 1 to add a value")
    print("Type 2 to delete a value")
    print("Type 3 to show the stack")
    print("Type 4 to end the program")
    option=int(input("Enter a number: "))
    return option

opt=0
while opt!=4 :
    opt=getoption()
    if opt == 1:
        letter=input("Enter a letter to add: ")
        push(letter)
    elif opt==2:
        pop()
    elif opt==3 :
        showStack()