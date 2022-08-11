import sys
import math

def isPrime(num):
        if(num%2==0):
                return False
        for i in range(3,int(math.sqrt(num))+1,2):
                if(num%i==0):
                        return False
        return True

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
		print(num)
	return sbArr

try:
	print(findSnowball(sys.argv[1]))
except:
	allFound=[]
	for i in [1,2,3,5,7]:
		allFound+=findSnowball(i)
	print("\n\nBiggest Snowball Prime Number Possible: ",max(allFound))
