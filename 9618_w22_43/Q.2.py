class Card():
    # declare self.__Number : Integer
    # declare self.__Colour : string
    def __init__(self, num , colour):
        self.__Number = num
        self.__Colour = colour

    def GetColour(self):
        return self.__Colour
    
    def GetNumber(self):
        return self.__Number
    
class Hand():
    # declare card1, card2, card3, card4, card5 of Type Card 
    # declare NumberCards, FirstCard : integer
    def __init__(self, card1, card2, card3, card4, card5):
        self.__FirstCard = 0
        self.__NumberCards = 5
        self.__Cards = []

        self.__Cards.append(card1)
        self.__Cards.append(card2)
        self.__Cards.append(card3)
        self.__Cards.append(card4)
        self.__Cards.append(card5)
    
    def GetCard(self, index):
        return self.__Cards[index]
    
#MAIN
for i in range(15):
    Card1 = Card(1, 'red')
    Card2 = Card(2, 'red')
    Card3 = Card(3, 'red')
    Card4 = Card(4, 'red')
    Card5 = Card(5, 'red')

    Card6 = Card(1, 'blue')
    Card7 = Card(2, 'blue')
    Card8 = Card(3, 'blue')
    Card9 = Card(4, 'blue')
    Card10 = Card(5, 'blue')

    Card11 = Card(1, 'yellow')
    Card12 = Card(2, 'yellow')
    Card13 = Card(3, 'yellow')
    Card14 = Card(4, 'yellow')
    Card15 = Card(5, 'yellow')

Player1 = Hand(Card1, Card2, Card3, Card4, Card11)
Player2 = Hand(Card12, Card13, Card14, Card15, Card6)

def CalculateValue(hand):
    PlayersScore = 0 
    for i in range(5):
        val = hand.GetCard(i)
        answer = val.GetColour()
        num = val.GetNumber()
        if answer == 'red':
            PlayersScore += 5
        elif answer == 'blue':
            PlayersScore += 10
        elif answer == 'yellow':
            PlayersScore += 15
        PlayersScore += num

    return PlayersScore

Score1 = CalculateValue(Player1)
Score2  =CalculateValue(Player2)
if Score1 > Score2:
    print('Player1 wins')
elif Score1 < Score2:
    print('Player2 wins')
else:
    print("It was a tie")