import random
W = '\33[0m'
R = '\33[31m'
G = '\33[32m'
O = '\33[33m'
B = '\33[34m'
P = '\33[35m'
color = [W, R, G, O, B, P]
a = 1
b = 1
choice2 = []
n = 0
N = 0
while (N <= 0) or (n <= 0) or (N <= n):
    n = int(input("How many color do you want (below or equals to 6)? \n"))
    col = color[:n]
    N = int(input("How many integer...(above the number of colors)\n"))

for i in range(1, N + 1):
    choice = random.choice(col)
    print(choice, i, end=" ")
    choice2.append(choice)
