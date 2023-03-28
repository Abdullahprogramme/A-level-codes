class Picture():
    def __init__(self, description, width, height, fc):
        self.__description = description     #string
        self.__width = int(width)           #integer
        self.__height = int(height)           #integer
        self.__framecolour = fc        #string

    def getdescription(self):
        return self.__description
    
    def getheight(self):
        return self.__height

    def getwidth(self):
        return self.__width

    def getframecolour(self):
        return self.__framecolour

    def setdescription(self, newdescription):
        self.__description = newdescription

#Main
count = 0
def ReadData(PictureArray):
    global count
    filename = "Pictures.txt"
    try:
        file = open(filename, 'r')
        description = file.readline().strip().lower()
        while description != "":
            
            width = int(file.readline().strip())
            height = int(file.readline().strip())
            framecolour = file.readline().strip().lower()

            PictureArray[count] = Picture(description, width, height, framecolour)
            
            description = file.readline().strip()
            count += 1
        
        file.close()
    except:
        print("File not found")
    return count , PictureArray

PictureArray = []
for i in range(0, 100):
    PictureArray.append(Picture("", 0, 0, ""))
number, PictureArray = ReadData(PictureArray)

color = input("Enter the colour: ").lower()
pWidth = int(input("Enter max width: "))
pheight = int(input("Enter max height: "))
for i in range(0, number):
    h = PictureArray[i].getheight()
    w = PictureArray[i].getwidth()
    fc = PictureArray[i].getframecolour()
    if fc == color:
        if h <= pheight:
            if w <= pWidth:
                print("Description: ", PictureArray[i].getdescription())
                print("Height: ", PictureArray[i].getheight())
                print("Width: ", PictureArray[i].getwidth())
                