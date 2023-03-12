lst = [9, 4, 6, 0, 7]
def bubble():
    for i in range(5):
        for j in range(5):
            if lst[i] < lst[j]:
                    temp  = lst[i]
                    lst[i] = lst[j]
                    lst[j] = temp
bubble()
lst1 = [9, 4, 6, 0, 7]
def Bumbo():
    Swap = False
    Item = len(lst1)
    while Swap == False:
        Swap = True
        for i in range(Item - 1):
            if lst1[i] > lst1[i + 1]:
                Swap = False
                temp = lst1[i]
                lst1[i] = lst1[i + 1]
                lst1[i + 1] = temp
        Item -=1
Bumbo()

print(lst)
print(lst1)