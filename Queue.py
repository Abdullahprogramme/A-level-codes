Q=[]
for i in range(10):
    Q.append(0)

Rp = -1
Fp = -1 
Size = -1
def EnQ(Val):
    global Size, Rp
    Max= 9
    if Size==Max:
        print("Queue is maxed")
    else:
        if Rp == Max :
            Rp = 0
        else:
            Rp += 1
        Q[Rp]=Val
        Size += 1
        print(Val , "added")

def DeQ():
    global Size, Fp
    Max = 9
    if Size == 0:
        return "Empty"
    else:
        if Fp == Max :
            Fp = 0
        else:
            Fp += 1
        x=Q[Fp]
        Size -= 1
        Q[Fp] = 0
        print("data deleted")
        return x

def getOption():
    print("Enter 1 to add data ")
    print("Enter 2 to add data ")
    print("Enter 3 show queue ")
    print("Enter 4 to end program ")
    Option=int(input("Enter the option here: "))
    return Option

def ShowQueue():
    for i in range(9,-1,-1):
        print(i , " " , Q[i])



#Main program
opt = -1
while opt != 4 :
    opt =getOption()
    if opt ==1 :
        Value=input("Enter the value to add in queue: ")
        EnQ(Value)
    elif opt == 2 :
        returnValue=DeQ()
        if returnValue== "Empty":
            print("Queue is empty ")
        else:
            print(returnValue , "deleted ")
    elif opt == 3:
        ShowQueue()
