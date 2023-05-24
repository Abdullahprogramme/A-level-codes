Array = ['','','','','','','','','','']  #String
head = 0 #Integer
tail = 0  #Integer
NoOfItems = 0   #Integer

def Enqueue(Array,head,tail,NoOfitems, DataToAdd):
    if NoOfitems >= 10:
        return (False, Array, head, tail, NoOfitems)
    Array[tail] = DataToAdd
    if tail >= 9:
        tail = 0
    else: tail =+ 1
    NoOfitems =+ 1
    return (True, Array, head, tail, NoOfitems)

def Dequeue(Array,head,tail,NoOfitems):
    if NoOfitems == 0:
        return (False, Array, head, tail, NoOfitems)
    removedItem = Array[head]
    if head >= 9:
        head = 0
    else: head =+ 1
    NoOfitems =- 1
    return (removedItem, Array, head, tail, NoOfitems)

for i in range(11):
    data = input('Enter a data to add in queue: ')
    Flag, Array, head, tail, NoOfItems = Enqueue(Array, head, tail, NoOfItems, data)
    if Flag is True:
        print('addition was succesful')
    else: print('addition was unsuccesful')
value , Array, head, tail, NoOfItems = Dequeue(Array, head, tail, NoOfItems)
print(value)
value , Array, head, tail, NoOfItems = Dequeue(Array, head, tail, NoOfItems)
print(value)