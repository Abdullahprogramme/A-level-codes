class HiddenBox():
    #private BoxName as stirng
    #private Creator as string
    #private DateHidden as string
    #private GameLocation as string
    #LastFinds : array[10][2] as string
    #private Active as boolean

    def __init__(self ,BoxName ,Creator ,DateHidden , GameLocation):
        self.__BoxName = BoxName
        self.__Creator = Creator
        self.__DateHidden = DateHidden
        self.__GameLocation = GameLocation
        self.__Active = False
        self.__LastsFind = [[''for i in range(2)] for j in range(10)]

    def GetBoxName(self):
        return self.__BoxName
    def GetGameLocation(self):
        return self.__GameLocation

#MAIN

TheBoxes = [HiddenBox("", "", "", "") for i in range(10000)]

def NewBox(TheBoxes, NumBoxes):
    name = input('Enter a name: ')
    creator = input('Enter a creators name: ')
    date = input("Enter the date: ")
    location = input("Enter the location: ")
    obj = HiddenBox(name, creator, date, location)
    TheBoxes[NumBoxes] = obj
    return NumBoxes + 1

NumBoxes = NewBox(TheBoxes, NumBoxes)

class PuzzleBox(HiddenBox):
    #private PuzzleText as string
    #private Solution as string
    def __init__(self ,BoxName ,Creator ,DateHidden , GameLocation ,PuzzleText , Solution):
        super.__init__(BoxName ,Creator ,DateHidden , GameLocation)
        self.__PuzzleText = PuzzleText
        self.__Solution = Solution