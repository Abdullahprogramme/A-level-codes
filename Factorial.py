#Iterative factorial

x = int(input("Enter a number here: "))
def Factorial(num):
    F =1
    for i in range(num, 0, -1): #or " for i in range(1 ,num + 1)"
        F = F * i
    print(F)
Factorial(x)

#Recursive factorial

def RecFactorial(num):
    if num == 1:
       return 1 
    else:
        return num * RecFactorial(num - 1)

answer = RecFactorial(x)
print(answer)