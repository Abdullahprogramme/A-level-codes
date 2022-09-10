Names=[]
Ages=[]
for Count in range(6):
    name=str(input("Input a name: "))
    Names.append(name)
    age=int(input("Input your age: "))
    Ages.append(age)
for Count in range(6):
    print(" The name is " + Names[Count] + " and age is " + str(Ages[Count]))