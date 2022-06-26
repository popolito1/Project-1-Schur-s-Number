n=0
fact=1
while (n<6):
    n=int(input("Enter n in order to bound S(n) (above or equals to 6) \n"))
    
left = (3**n-1)//2
for i in range (1,n+1):
    fact = fact*i
  
right = 3*fact-1
print("The intervals is :\n")
print(left,"<= S(",n,") <=",right)
    