Names=[]
for i in range(2):
    name=input("Input a name :   ")
    Names.append(name)
Counts={}
print(Names)
for word in Names:
    #if word not in Counts:
        #Counts[word]= 1
    #else:
        #Counts[word]=Counts[word] + 1
    Counts[word]=Counts.get(word,0) + 1
print(Counts)
print(Counts["Abdullah"])