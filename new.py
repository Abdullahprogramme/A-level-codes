left = [-1, -1, -1, -1, -1, -1, -1]
data = [0, 0, 0, 0, 0, 0, 0]
right = [-1, -1, -1, -1, -1, -1, -1]

fp = 0
root = 0
def banayritreeeee(val):
    global fp, root
    cn = root
    added = False
    if fp > 6:
        print("Overflow occured")
    elif fp == 0:
            data[fp] = val
            fp =+ 1
    else:
        data[fp] = val
        while added is False:
            if val < data[cn]:
                if left[cn] == -1:
                    added = True
                    left[cn] = fp
                else:
                    cn = left[cn]

            elif val > data[cn]:
                if right[cn] == -1:
                    added = True
                    right[cn] = fp
                else:
                    cn = right[cn]
        fp = fp + 1

def banayriSurch(value):
    current = 0
    isFound = False
    while current != -1 and isFound is False:
        if value == data[current]:
            isFound = True
        elif value < data[current]:
            current = left[current]
        elif value > data[current]:
            current = right[current]
    if isFound is True:
        return current
    else:
        return -1
    
def trevor(root):
    if root != -1:
        trevor(left[root])
        print(data[root])
        trevor(right[root])
#MAIN
for i in range(6):
    word = int(input("Enter data to enter"))
    banayritreeeee(word)

x = banayriSurch(6)
print("Found at"+ str(x))

for i in range(6):
    print(left[i], "   ", data[i], "  ", right[i])
trevor(0)