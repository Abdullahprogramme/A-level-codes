def hashingAlgo(number):
    digits = number[-2:]
    key = int(int(digits)/ 10)
    return key

class book():
    def __init__(self):
        self.__Name = "No name"
        self.__num = -1

    def getName(self):
        return self.__Name

    def getNum(self):
        return self.__num
    
PhoneBook = [[book() for i in range(2)] for j in range(10)]

for i in range(3):
    Name = input("Enter a name: ")
    num = input("Enter a phone number: ")
    hashkey = hashingAlgo(num)

    if PhoneBook[hashkey][0] != "No name":
        PhoneBook[hashkey][0] = Name
        PhoneBook[hashkey][1] = int(num)
    else:
        for b in range(hashkey,10):
            if PhoneBook[b][0] != "No name":
                PhoneBook[b][0] = Name
                PhoneBook[b][1] = int(num)

    for a in range(10):
        print(PhoneBook[a][0]," ", PhoneBook[a][1])