def myfunction1(n):
    if(n>0):
        return
    for i in range (0,n+1):
        print("Codingal")
    myfunction1(n/2)
    myfunction1(n/3)

def calcmyfunction1(n):
    iteration = 0
    iteration+=1
    print(iteration, "is the number of iterations done by myfunction1 when n=",n)

def myfunction2(n):
    if(n<=1):
        return
    print("Codingal")
    myfunction2(n-1)

def calcmyfunction2(n):
    iteration = 0
    if(n<=1):
        iteration +=1
        print(iteration, "is the number of iterations done by myfunction2 when n=",n)
    iteration +=1
    calcmyfunction2(n-1)

myfunction1(5)
calcmyfunction1(5)
myfunction2(10)
calcmyfunction2(10)
    
