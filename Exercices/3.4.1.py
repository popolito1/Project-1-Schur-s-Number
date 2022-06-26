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
n=2
N=2
a=1
b=1
mono="True"

for i in range (N):
        while (a<=N) and (b<=N):
            if (a+b<=N):
                print ("(",a,b,a+b,")")
                b += 1
            if (b>=N):
                a += 1
                b=a
            Triplet = a,b,a+b
        triplet.append(Triplet)
        A = True
    
comb = n**N    
print("The possible combinations is:",comb)
for j in range (0,comb):
    while j>(n-1):
        number.append(j%n)
        j=j//n
    number.append(j)
    number.reverse()  
    allnumber.append(number) 
    number=[]                         #Empty the list "number"
    
for k in allnumber:                            #to have the same size
    while (len(k)<len(allnumber[len(allnumber)-1])):
        k.insert(0,0)
        
for l in allnumber:
    for m in l:
        print(color[m],numbers,end="")
        numbers+=1
    numbers=0
    print("")
    

for i in triplet:
    if (B):
        print ("\n Your triplet is monochromatic")
        print ("(",a,x,b,y,c,z,")")
    else:
        A=False
    if (A):
        print("the result is: S(",n,"=",N-1)
  
a=len(monochromatic)
if (a==0):                                                    # so if one triplet is monocromatic it displays = False
    print (W,"None are monochromatic \n")                    # So I initialize test = True            
else:
    print (W,"All or one triplet(s) are/is monochromatic(s) \n")
    test="False"
print("\n",test)
    
    
    
    
  