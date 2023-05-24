class Card():
    #Private __Number  as Integer
    #Private __Colour  as String
    def __init__(self, number, color):
        self.__Number = number
        self.__Colour = color

    def GetNumber(self):
        return self.__Number
    
    def GetColour(self):
        return self.__Colour
    
#Main
NumberChosen = [False for i in range(30)]

CardArray = [Card(0,'') for i in range(30)]
try:
    file = open("CardValues.txt", 'r')
    for i in range(30):
        data1  = int(file.readline())
        data2 = file.readline()
        CardArray[i] = Card(data1, data2)
    file.close()
except:
    print("File not found")

def ChooseCard():
    integer = 0
    while integer < 1 or integer > 30:
        integer = int(input('Enetr a number: '))
    
    flag = False
    while flag == False:
        if NumberChosen[integer - 1] == False:
            NumberChosen[integer - 1] = True
            print("Valid")
            flag = True
        else:
            print("Already chosen")
            integer = 0
            while integer < 1 or integer > 30:
                integer = int(input('Enetr a number: '))
    return integer - 1

Player1 = [] # of type Card
for i in range(4):
    num = ChooseCard()
    Player1.append(CardArray[num])

for i in range(4):
    print("Number is: ", Player1[i].GetNumber(), " and colour is ", Player1[i].GetColour())