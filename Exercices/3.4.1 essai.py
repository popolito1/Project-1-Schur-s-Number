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
mono = []
test = "True"
numbers=0
n=2
N=2
p=10
a=1
b=1

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
for q in range (N):
    while a+b<=N:                                                   
        A = random.choice (color)                                   
        B = random.choice (color)
        C = random.choice (color)
        if (A==B) and (B==C):
            mono.append(A)
        if (a+b<=N):
            print ("(",A,a,B,b,C,a+b,")",end=" ")
            b += 1
        if (b>=N):                                                  
            a += 1       
            b=a                                             # True = all triplet are not monochromatic 
a=len(mono)
if (a==0):                                                    # so if one triplet is monocromatic it displays = False
    print (W,"None are monochromatic \n")                    # So I initialize test = True            
else:
    print (W,"All or one triplet(s) are/is monochromatic(s) \n")
    test="False"
print("\n",test)
print ("S(",n,") =",N-1)

        