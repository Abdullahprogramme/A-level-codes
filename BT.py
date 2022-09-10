#Declare record type 
class Tree:
    def __init__(self):
        self.lp=0
        self.data=""
        self.rp=0
BT=[Tree() for i in range(10)] # Make a 2d array of type Tree
# initialize the Binary tree 
def initialize():
    global fp,root
    for i in range(10):
        BT[i].lp=-1
        BT[i].data=-1
        BT[i].rp=-1
    fp=0
    root=0
def Insert(Val):
    global fp
    cn=root
    isAdded=False
    if BT[cn].data==-1 :
        BT[cn].data=Val
        fp = fp + 1
    elif fp > 9:
        print("No more space to insert more data")
    else:
        BT[fp].data= Val
        while isAdded == False:
            if Val < BT[cn].data:
                if BT[cn].lp == -1:
                    isAdded = True
                    BT[cn].lp= fp
                else:
                    cn=BT[cn].lp
            elif Val > BT[cn].data:
                if BT[cn].rp== -1:
                    isAdded= True 
                    BT[cn].rp= fp
                else:
                    cn= BT[cn].rp
        fp = fp + 1 
def binarySearch(Value):
    current=0
    isFound = False
    while current != -1 and isFound == False:
        if Value == BT[current].data:
            isFound = True
        elif Value < BT[current].data:
            current= BT[current].lp
        else:
            current = BT[current].rp
    if isFound == True:
        return current
    else:
        return -1

null= -1
root=0
fp=0

def traverse(root):
    if root!= null:
        traverse(BT[root].lp)
        print(BT[root].data)
        traverse(BT[root].rp)

# Use this one area

#initialize()
#for i in range(10):
    #x=int(input("Enter the number you want to insert in BT: "))
    #Insert(x)

#for i in range(10):
    #print(BT[i].lp,BT[i].data,BT[i].rp)
 
#traverse(root)



# or this one area
initialize()
num=[5,3,7,1,2,8,4,0,9,6]
for number in num:
    Insert(number)

for i in range(10):
    print(BT[i].lp,BT[i].data,BT[i].rp)

traverse(0)
x=binarySearch(7)
print("found at ", x)