global StackData #Integer
global StackPointer
StackData = [0,0,0,0,0,0,0,0,0,0]
StackPointer = 0 #Integer

def Output():
    global StackPointer, StackData
    for i in range(10):
        print(StackData[i])
    print('Stack Pointer is: ', StackPointer)

def Push(Value):
    global StackData, StackPointer
    if StackPointer == 10:
        print("stack is full")
        return False
    else:
        StackData[StackPointer] = Value
        StackPointer += 1
        return True

def Pop():
    global StackData, StackPointer
    if StackPointer == 0:
        print('Stack is empty')
        return -1
    else:
        value = StackData[StackPointer - 1]
        StackPointer -= 1
        return value

#MAIN
for i in range(11):
    number = int(input('Enter a number to enter in a stack: '))
    answer = Push(number)
    if answer is True:
        print("Value correctly pushed")
    else:
        print('Value cannot be pushed')
Output()
answer = Pop()
if answer == -1:
    print("Data not popped")
else: print("Data popped")
answer = Pop()
if answer == -1:
    print("Data not popped")
else: print("Data popped")