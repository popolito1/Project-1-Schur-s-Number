W = '\33[0m'
R = '\33[31m'
G = '\33[32m'
O = '\33[33m'
B = '\33[34m'
P = '\33[35m'
color = [W,R,G,O,B,P]
n=0
while (n<=0) :
    n=int(input("How many numbers you want to color ? \n"))

for i in range (1, n+1):
    if (i%2==0):
        print(R, i, end=" ")
    else:
        print(B, i, end=" ")

