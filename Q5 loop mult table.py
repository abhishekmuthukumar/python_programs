#Q5 loop mult table

x= int(input("enter the start table"))

y= int(input("enter the end table "))
for i in range(x,y+1):
     for j in range(0,11):
         print(i, "*",j, "=",i*j)
