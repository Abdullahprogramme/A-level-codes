lst=[]
for A in range(8):
    number = int(input("Enter a number here:  "))
    lst.append(number)
print(lst)
Found = False
i = 0
def LinearSearch(Val):
    global Found , i
    while Found == False and i != 8:
        if lst[i] == Val:
            Found = True
        i = i + 1
    if Found == True:
        return i - 1
    else:
        return -1
value = int(input("Enter the value you want to search:  "))
answer = LinearSearch(value)
if answer == -1:
    print("Value not found in array")
else:
    print("Value found at " ,answer)