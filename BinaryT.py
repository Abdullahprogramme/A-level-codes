left = [-1 , -1, -1, -1, -1, -1, -1, -1, -1, -1]
data = [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ]
right = [-1 , -1, -1, -1, -1, -1, -1, -1, -1, -1]

root = 0
fp = 0
def add(val):
    global fp ,root
    if fp > 9:
        print("overflow occured")
    else:
        cn =root
        if fp == 0:
            data[fp] = val
            fp += 1
        else:
            pn =0
            direction = " "
            data[fp] = val
            while cn != -1:
                pn = cn
                if val > data[cn]:
                    direction = "r"
                    cn = right[cn]
                elif val < data[cn]:
                    direction = "l"
                    cn = left[cn]
            if direction == "r":
                right[pn] = fp
            elif direction == "l":
                left[pn] = fp
            fp += 1

def View():
    for i in range(10):
        print(" pointer:", i, left[i], data[i], right[i])

for i in range(10):
    x = int(input("enter a number: "))
    add(x)

View()
def traversal(root):
    if root!= -1 :
        traversal(left[root])
        print(data[root])
        traversal(right[root])
traversal(0)