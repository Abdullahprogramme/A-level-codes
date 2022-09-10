def search(UB,array,LB,Val):
    IsFound=False
    while IsFound != True:
        mid=int((UB + LB)/2)
        if Val == array[mid]:
            IsFound= True
        elif Val < array[mid]:
            UB= mid -1 
        elif Val > array[mid]:
            LB= mid + 1 
    return mid

def searchRec(UB,array,LB,Val):
    mid=int((UB + LB)/2)
    if Val == array[mid]:
        return mid
    elif Val < array[mid]:
        return searchRec(mid - 1, array, LB, Val)
    elif Val > array[mid]:
        return searchRec(UB, array, mid + 1, Val)

lst=[]
for i in range(10):
    words=input("Enter a word to add: ")
    lst.append(words)

word=input("Enter a word to search: ")

answer1=search(9 ,lst,0,word)
answer2=searchRec(9,lst,0,word)

print("Found at: ", answer1)
print("Found at: ", answer2)