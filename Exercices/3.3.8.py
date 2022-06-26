number = -1
b = -1
while (number<0): 
    number=int(input("Enter your number \n "))
while (b<=1):
    b=int(input("Enter your wanted base >1 \n "))
    
if (number==0) :
    print ("Your number in the conversion system is 0")   
else:
    reste=[]
    print("your number in base",b,"is:")
    while (number!=0):
        quotient=number//b
        r=number%b
        number=quotient
        if (r==10):
            r="A"
        if (r==11):
            r="B"
        if (r==12):
             r="C"
        if (r==13):
            r="D"
        if (r==14):
            r="E"
        if (r==15):
            r="F"
        if (r==16):
            r="G"
        if (r==17):
            r="H"
        if (r==18):
            r="I"
        if (r==19):
            r="J"
        if (r==20):
            r="K"
        if (r==21):
            r="L"
        if (r==22):
            r="M"
        if (r==23):
            r="N"
        if (r==24):
            r="O"
        if (r==25):
            r="P"
        if (r==26):
            r="Q"
        if (r==27):
            r="R"
        if (r==28):
            r="S"
        if (r==29):
            r="T"
        if (r==30):
            r="U"
        if (r==31):
            r="V"
        if (r==32):
            r="W"
        if (r==33):
            r="X"
        if (r==34):
            r="Y"
        if (r==35):
            r="Z"
        reste.append(r)
    reste.reverse()
    print(reste)
        