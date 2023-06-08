#09 REST BILL

f=int (input (" enter the food rating 1-5' :"))
s=int (input(" enter the serviece rating '1-5' :"))
a=int (input (" enter the ambiance rating '1-5' :"))
b=int (input ("enter the bill amount :"))
if (f>=4):
    if (s>=4 and a>=4):
        print(" THE BILL AMOUNT IS :",b+((b*10)/100))
    elif(s<=3 and a>=3):
        print("THE BILL AMOUNT IS :" ,b+((b*5)/100))
elif(f<=3):
    if(s>=4 and a>=4):
        print("THE BILL AMOUNT IS :",b+((b*5)/100))
    elif(s<=3 and a>=3):
        print("THE BILL AMOUNT IS :",b+((b*1)/100))
    
