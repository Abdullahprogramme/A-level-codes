HighScoreArray = [[ ''for column in range(2)]for rows in range(11)]

def ReadHighScores():
    filename = 'Highscore.txt'
    file = open(filename)
    for count in range(10):
        line1 = file.readline().strip()
        line2 = file.readline().strip()
        HighScoreArray[count][0] = line1
        HighScoreArray[count][1] = line2
    file.close()

def OutputHighScore():
    for i in range(10):
            print(HighScoreArray[i][0] + ' ' + str(HighScoreArray[i][1]))

ReadHighScores()
OutputHighScore()

NewName = input('Enter a name : ')
while len(NewName) != 3:
    NewName = input('Enter a name : ')

NewScore = input('Enter a score : ')
while int(NewScore) < 1 or int(NewScore) > 100000:
    NewScore = input('Enter a score : ')


def Sort(NewName, NewScore):
    HighScoreArray[10][0] = NewName
    HighScoreArray[10][1] = NewScore
    for x in range(11):
        temp1 = HighScoreArray[x][0]
        temp2 = HighScoreArray[x][1]
        pointer = x - 1
        while int(temp2) > int(HighScoreArray[pointer][1]) and pointer > -1:
            HighScoreArray[pointer + 1][0] = HighScoreArray[pointer][0]
            HighScoreArray[pointer + 1][1] = HighScoreArray[pointer][1]
            pointer = pointer - 1
        HighScoreArray[pointer + 1][0] = temp1
        HighScoreArray[pointer + 1][1] = temp2

Sort(NewName, NewScore)
OutputHighScore()

def WriteTopTen():
    file = open('NewHighScore.txt','w')
    for i in range(10):
        line1 = HighScoreArray[i][0]
        line2 = HighScoreArray[i][1]
        file.write(line1 + '/n')
        file.write(line2 + '/n')
    file.close()
