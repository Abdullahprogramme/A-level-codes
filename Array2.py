Test1=[]
Test2=[]
Test3=[]
TotalMarks=[]
Name=[]
Highest=0
for Count in range(2):
    print("Input your name")
    name=str(input())
    print("Input your Test 1 marks")
    test1=str(input())
    print("Input your Test 2 marks")
    test2=str(input())
    print("Input your Test 3 marks")
    test3=str(input())
    totalmarks = int(test1) + int(test2) + int(test3)
    Test1.append(test1)
    Test2.append(test2)
    Test3.append(test3)
    TotalMarks.append(totalmarks)
    if totalmarks > Highest:
        Highest = totalmarks
Count=0             
for Count in range(2):
    print("Students name is " + Name[Count] + " his score is " + TotalMarks[Count] + " out of 75 ")
    if Highest == TotalMarks[Count]:
        print("The highets marks are " + str(Highest) + " and students name is " + str(Name[Count]))
