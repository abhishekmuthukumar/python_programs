#LOOPING Q1 OC and EC COUNT
ec=0
oc=0

for i in range (20,50):
    if(i%2==0):
        ec=ec+1
    else:
        oc=oc+1



print ("THE TOTAL NUMBER OF ODD NUMBER IN THE RANGE IS :",oc)
print ("THE TOTAL NUMBER OF EVEN NUMBER IN THE RANGE IS :",ec)
