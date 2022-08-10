sPoint = int(input("Enter Starting Point: "))

def isPrime(num):
        for i in range(2,num-1):
                if(num%i==0):
                        return(False)
        return(True)

def findSnowball(num,sba=[]):
        sbArr=sba
        found=False
        for i in range(1,10,2):
                n = int(str(num)+str(i))
                if(isPrime(n)):
                        found = True
                        findSnowball(n,sbArr) 
        if(not found):
                sbArr.append(num) 
        return sbArr

print(findSnowball(sPoint))
