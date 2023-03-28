class Character():
    #Self.self.__Name as string
    #self.__XCoordinate as integer
    #self.__YCoordinate as integer

    def __init__(self, name, x , y):
        self.__Name = name
        self.__XCoordinate = x
        self.__YCoordinate = y

    def GetName(self):
        return self.__Name 
    
    def GetX(self):
        return self.__XCoordinate 
    
    def GetY(self):
        return self.__YCoordinate 

    def ChangePosition(self, Xchange, Ychange):
        self.__YCoordinate += Ychange
        self.__XCoordinate += Xchange
    
#Main
CharArray = []
try:
    file = open("Characters.txt", 'r')
    for i in range(10):
        name = file.readline().strip()
        x = file.readline().strip()
        y = file.readline().strip()
        obj = Character(name, int(x), int(y))
        CharArray.append(obj)
    file.close()
except:
    print("File not found")

num = -1
while num == - 1:
    UserName = input('Enter a name').rstrip().lower()
    for i in range(10): 
        if UserName == CharArray[i].GetName().strip().lower():
            temp = i
            num  = 1
        

IsValid = False
while IsValid == False:
    letter = input("Enter A for left, W for up, S for down, D for right : ")
    if letter.upper() == 'A':
        CharArray[temp].ChangePosition(-1, 0)
        IsValid = True
    elif letter.upper() == 'W':
        CharArray[temp].ChangePosition(0, 1)
        IsValid = True
    elif letter.upper() == 'S':
        CharArray[temp].ChangePosition(0, -1)
        IsValid = True
    elif letter.upper() == 'D':
        CharArray[temp].ChangePosition(1, 0)
        IsValid = True
    

print(CharArray[temp].GetName().lower(), " has changed coordinates to X = ",CharArray[temp].GetX() ," and Y = ", CharArray[temp].GetY())