import random
W = '\33[0m'
R = '\33[31m'
G = '\33[32m'
O = '\33[33m'
B = '\33[34m'
P = '\33[35m'
color = [W,R,G,O,B,P]
a=1
b=1
choice2=[]
n=0
N=0
while (N<=0) or (n<=0) or (N<=n):
    n=int(input("How many color do you want (below or equals to 6)? \n"))
    col=color[:n]
    N=int(input("How many integer...(above the number of colors)\n"))
    
for i in range (1, N+1):
    choice = random.choice(col)
    print(choice,i,end= " ")
    choice2.append(choice)
A = choice2.count('\33[0m')
B = choice2.count('\33[31m')
C = choice2.count('\33[32m')
D = choice2.count('\33[33m')
E = choice2.count('\33[34m')
F = choice2.count('\33[35m')
G = [A,B,C,D,E,F]
while(0 in G):                      #if the colour are not used, it count 0 so the loop serves to delete in the list when it's 0
    if 0 in G:
        G.remove(0)       
if (len(G)==n):
    print(W,"\nThe colouring is valid")
else:
    print(W,"\nThe colouring is not valid") 