#Declare record type  to maka binary tree as a linked list
class BTnode:
   def __init__(self):
        self.LP = -1
        self.data = 0
        self.RP = -1
BT = [BTnode() for i in range(10)] # make a 2d array of type BTnode
null = -1
def initialize():
    global fp,root
    for i in range(10):
        BT[i].LP= null
        BT[i].data=0
        BT[i].RP= i + 1
    BT[9].RP = null
    fp=0
    root=0


def insert(val):
    global fp
    cn = root
    isAdded = False
    if BT[cn].data == 0:
        BT[cn].data = val
        fp = BT[cn].RP
        BT[cn].RP = null
    elif fp > 9:
        print("tree is full")
    else:
        BT[fp].data = val
        pp = fp
        a = BT[pp].RP
        BT[pp].RP = null
        while isAdded == False:
            if val < BT[cn].data:
                if BT[cn].LP == null:
                    isAdded = True
                    BT[cn].LP= fp
                else:
                    cn=BT[cn].LP
            elif val > BT[cn].data:
                if BT[cn].RP== null:
                    isAdded= True 
                    BT[cn].RP= fp
                else:
                    cn= BT[cn].RP
        fp = a
def BinarySearch(value):
    current=0
    isFound = False
    while current != null and isFound == False:
        if value == BT[current].data:
            isFound = True
        elif value < BT[current].data:
            current= BT[current].LP
        else:
            current = BT[current].RP
    if isFound == True:
        return current
    else:
        return null

def traverse(root):
    if root!= null:
        traverse(BT[root].LP)
        print(BT[root].data)
        traverse(BT[root].RP)
initialize()
print(" Pointers", " leftP", "  data" , "  RightP")
for i in range(10):
    print("Pointer"+str(i)  ,"   " ,BT[i].LP,"    " , BT[i].data,"   " ,BT[i].RP)
print("  ")
num=[5,3,7,1,2,8,4,0,9,6]
for number in num:
    insert(number)
print(" Pointers", " leftP", "  data" , "  RightP")
for i in range(10):
    print("Pointer"+str(i)  ,"     " ,BT[i].LP,"    " , BT[i].data,"   ",BT[i].RP)
print("Traversed BT")
traverse(0)
for i in range(2):
    x =int(input("Enter a number to search : "))
    answer = BinarySearch(x)
    print("found at pointer" ,answer)