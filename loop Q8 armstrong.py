#printing armstrong number btw 100 to 1000
for x in range (100,1000):
    temp=x
    sum=0
    while temp>0:
        digit=temp%10
        sum=sum+digit**3
        temp=temp//10
    if sum==x:
            print(sum)
        
