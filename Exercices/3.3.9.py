import random
R="\033[31m"
G="\033[32m"
O="\033[33m"
B="\033[34m"
P="\033[35m"
W="\033[0m"

color=[W,R,G,O,B,P]
num=0
number=[]
allnumber=[]
numbers=0
n=0
N=0

while (N<=0) or (n>6) or (n<=0):
    N=int(input("Enter a number \n"))       #number of bit
    n=int(input("Choose a number of color (below or equals to 6)\n"))    #number of color = base
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
    print("")               #stop the end                
    