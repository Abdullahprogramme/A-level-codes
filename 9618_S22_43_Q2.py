class Balloon():
    def __init__(self, colour, defence):
        self.__Health = 100 # Integer
        self.__Colour = colour # String
        self.__DefenceItem = defence # String
    
    def GetDefenceItem(self): #returns string
        return self.__DefenceItem

    def ChangeHealth(self, ChangeInHealth): 
        self.__Health += ChangeInHealth
    
    def CheckHealth(self): # retuns boolean
        if self.__Health <= 0: return True
        else: return False

#Main:
colour = input("Enter a colour for your balloon: ")
defenceitem = input("Enter a defence item for your balloon: ")
Balloon1 = Balloon(colour, defenceitem)

def Defend(BalloonOBJ):
    strength = int(input("Enter the strength of the opponent: "))
    BalloonOBJ.ChangeHealth(-strength)
    print("The defence item is ", BalloonOBJ.GetDefenceItem())
    if BalloonOBJ.CheckHealth() is True:
        print("Your balloon has no health remaining")
    elif BalloonOBJ.CheckHealth() is False:
        print("Your balloon has health remaining")
    return BalloonOBJ
Defend(Balloon1)