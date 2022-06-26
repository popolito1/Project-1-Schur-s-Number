import random
R="\033[31m"
G="\033[32m"
O="\033[33m"
B="\033[34m"
P="\033[35m"
W="\033[0m"

color=[W,R,G,O,B,P]
col=[W,R]
num=0
number=[]
allnumber=[]
N=2
n=2
a=1
b=1
asso =[]
numbers=0
allmono = True
onemono = True
trip = []
triplet = []
print ("The list of all the triplets is : \n ")
while (allmono):
    while (a<=N) and (b<=N):
        if (a+b<=N):
            print ("(",a,b,a+b,")")
            A=(a,b,a+b)
            b += 1
        if (b>=N):
            a += 1
            b=a
        trip.append(A)
        print(trip)
    allmono = False
    for i in range (0,N-1):
        num=n**N                                    #num corresponds to the number of possible combinations
        for j in range (0,num):                     #To L18 to L25 is the 3.3.8 (base n)
            while (j>=n):
                number.append(j%n)
                j=j//n
                number.append(j)
                number.reverse()  
                allnumber.append(number)
                number=[]                               #Empty the list "number" to fill again then
        for k in allnumber:                 
            while (len(k)<len(allnumber[len(allnumber)-1])):        # size (k) <  size(size of the list -1) 
                k.insert(0,0)
        
        for l in allnumber:
            for m in l:            #make a tour in the colors    
                print(color[m],numbers+1,end="")
                numbers+=1
            numbers=0
            print("")
            #stop the end                