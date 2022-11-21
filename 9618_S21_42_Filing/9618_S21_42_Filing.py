class TreasureChest():
    def __init__(self, Q, A, Pts):
        self.__Question = Q
        self.__Answer = A
        self.__Points = Pts

    def getQuestion(self):
        return self.__Question
    
    def CheckAnswer(self, answer):
        if self.__Answer == answer: return True
    
    def getPoints(self, NoOfAttempts):
        LST = [ 1, 2, 3, 4]
        if NoOfAttempts == 1 : return self.__Points
        elif NoOfAttempts == 2 : return (self.__Points // 2)
        elif NoOfAttempts == 3 or NoOfAttempts == 4 : return(self.__Points // 4)
        elif NoOfAttempts not in LST : return 0
            
#Main
arrayTreasure = []
def readData():
    try:
        file = open('TreasureChestData.txt', 'rt')
        question = file.readline()
        while question != "":
            answer = file.readline()
            point = file.readline()
            obj = TreasureChest(question.strip(), int(answer.strip()), int(point.strip()))
            arrayTreasure.append(obj)
            question = file.readline()
        file.close()
    except:
        print("file not found")

readData()
QNumber = int(input('Enter a question number from 1 to 5: '))
if QNumber == 1 : 
    print(arrayTreasure[0].getQuestion())
    temp = 0
elif QNumber == 2 : 
    print(arrayTreasure[1].getQuestion())
    temp = 1
elif QNumber == 3 : 
    print(arrayTreasure[2].getQuestion())
    temp = 2
elif QNumber == 4 : 
    print(arrayTreasure[3].getQuestion())
    temp = 3
elif QNumber == 5 : 
    print(arrayTreasure[4].getQuestion())
    temp = 4
count = 0
check = False
answer = int(input("Enter your answer here: "))
check = arrayTreasure[temp].CheckAnswer(answer)
while check != True:
    check = arrayTreasure[temp].CheckAnswer(answer)
    count += 1
    answer = int(input("Enter your answer here again: "))

if count == 0:
    count = 1
point = arrayTreasure[temp].getPoints(count)
print('Your points are : ' + str(point))