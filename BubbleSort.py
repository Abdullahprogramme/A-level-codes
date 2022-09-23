lst=[]
for A in range(8):
    number = int(input("Enter a number here:  "))
    lst.append(number)
print(lst)
def BubbleSort():
    NoMoreSwaps = False
    NoItems = 8
    while NoMoreSwaps == False:
        NoMoreSwaps = True
        for i in range(NoItems-1):
            if lst[i] > lst[i + 1]:
                NoMoreSwaps= False
                Temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = Temp
        NoItems-=1
BubbleSort()
print(lst)