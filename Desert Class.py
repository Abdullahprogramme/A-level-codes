import random
import time
animal = 'A'
Food = 'F'
sand = '.'
class Desert():
    def __init__(self):
        self.__Grid = [[sand for across in range(15)] for down in range(15)]
        self.__AnimalList = []
        self.__stepCounter = 0 
        self.__NumberofAnimals = 0

        for i in range(5):
            self.GenerateAnimal()
        self.GenerateFood()

    def GenerateAnimal(self):
        if self.getNumberofAnimals() < 20:
            animals = Animal()
            self.setGrid(animals.GetAcross(), animals.GetDown(), animal)
            self.__AnimalList.append(animals)
            self.setNumberofAnimals()
    
    def setGrid(self, x, y, val):
        self.__Grid[y][x] = val

    def getGrid(self, a ,b):
        return self.__Grid[b][a]

    def getNumberofAnimals(self):
        return self.__NumberofAnimals

    def setNumberofAnimals(self):
        self.__NumberofAnimals += 1

    def IncrementStepCounter(self):
        self.__stepCounter += 1

    def DisplayGrid(self):
        for down in range(15):
            for across in range(15):
                print(self.__Grid[down][across], end = '')
            print()
    
    def GenerateFood(self):
        a = random.randint(0, 14)
        b =random.randint(0, 14)
        self.__Grid[b][a] = Food

    def Simulate(self):
        for i in range(100):
            for j in range(self.getNumberofAnimals()):
                self.__AnimalList[j].Move()
            time.sleep(2.5)
            self.DisplayGrid()
            print("#######################################################")
        for i in range(self.getNumberofAnimals()):
            print("Animal no:" , i , ' score = ', self.__AnimalList[i].GetScore())

class Animal():
    def __init__(self):
        x = random.randint(0, 14)
        y = random.randint(0, 14)
        self.__Across = x
        self.__Down = y
        self.__Score = 0
    
    def SetAcross(self, x):
        self.__Across = x
    
    def GetAcross(self):
        return self.__Across

    def SetDown(self, y):
        self.__Down = y

    def GetDown(self):
        return self.__Down

    def GetScore(self):
        return self.__Score

    def GenerateChangeInCoordinate(self, value):
            if value == 14:
                newPos = random.randint(-1, 0)
            elif value == 0:
                newPos = random.randint(0, 1)
            else:
                newPos = random.randint(-1, 1)
            return newPos

    def Move(self):
        desertObj.setGrid(self.__Across, self.__Down ,sand)
        self.__Across += self.GenerateChangeInCoordinate(self.__Across)
        self.__Down += self.GenerateChangeInCoordinate(self.__Down)
        if desertObj.getGrid(self.__Across, self.__Down) == Food:
            self.EatFood()
        desertObj.setGrid(self.__Across, self.__Down, animal)

    def EatFood(self):
        self.__Score += 1
        desertObj.GenerateFood()
        desertObj.GenerateAnimal()
#Main program
desertObj = Desert()
desertObj.Simulate()