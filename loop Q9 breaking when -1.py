ec=0
oc=0
for i in range(100):
    x=int(input("enter the number :"))
    if(x!=-1):
        if(x%2==0):
            ec+=1
        else:
            oc+=1
    else:
        break
print("the odd count is :",oc)
print("the even count is :",ec)
