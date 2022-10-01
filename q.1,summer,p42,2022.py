#initializing the stack structure
StackData=[]
a = 0
for i in range(11):
    StackData.append(a)
StackPointer = 0

#outputting all pointers
print("#StackPointer",StackPointer)
for i in range(11):
    print("Pointer ",i + 1,":",StackData[i])

def Push(val):
    global StackPointer, Flag
    Flag = True
    while StackPointer < 12:
        if StackPointer == 11:
            Flag = False
            print("Value cannot be added , stack is full")
            return Flag
        else:
            StackData[StackPointer] = val
            print(val, " Added in the stack at position ", StackPointer + 1)
            StackPointer += 1
            return Flag

for i in range(11):
    number = int(input("Enter the value here to enter it in the stack: "))
    Push(number)

#outputting all pointers
print("#StackPointer",StackPointer)
for i in range(11):
    print("Pointer ",i + 1,":",StackData[i])

def Pop():
    global StackPointer, Flag
    while StackPointer > -2:
        if StackPointer == 0:
           print("Stack is empty")
        else:
            RemovedVal = StackData[StackPointer -1]
            StackPointer -= 1
            print("Value popped from position", StackPointer + 1)
            return RemovedVal

answer = Pop()
answer = Pop()

#outputting all pointers
print("#StackPointer",StackPointer)
for i in range(11):
    print("Pointer ",i + 1,":",StackData[i])