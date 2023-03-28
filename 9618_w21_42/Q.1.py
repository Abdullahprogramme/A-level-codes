def Unknown(X,Y):
    if X < Y:
        print(str(X + Y))
        return (Unknown(X + 1, Y) * 2)
    elif X == Y:
        return 1
    else:
        print(X + Y)
        return int(Unknown(X - 1, Y) // 2)
def IterativeUnknown(x, y):
    total = 1
    while x != y:
        print(str(x + y))
        if x < y:
            x += 1
            total = total * 2
        elif x > y:
            x -= 1
            total = int(total / 2)
    return total
#Main

print("10 and 15") 
print(str(Unknown(10, 15))) 
print("10 and 10") 
print(str(Unknown(10, 10))) 
print("15 and 10") 
print(str(Unknown(15, 10)))
print("--------------------------------------------")
print("10 and 15") 
print(str(IterativeUnknown(10, 15))) 
print("10 and 10") 
print(str(IterativeUnknown(10, 10))) 
print("15 and 10") 
print(str(IterativeUnknown(15, 10)))
