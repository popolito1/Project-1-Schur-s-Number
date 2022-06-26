number = -1
while (number<0):
    number=int(input("Enter your decimal number \n "))

if (number==0):
    print ("Your number in binary system is O")
    
else:
    restofthedivision = []
    print("Your number in binary system is:")
    while (number!=0):
        quotient=number//2
        remainder=number%2
        number=quotient
        restofthedivision.append(remainder)
    restofthedivision.reverse()
    print(restofthedivision,end= " ",)
        
  

        
