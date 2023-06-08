w=int(input("enter the wind speed in kmph :"))
t=int(input("enter the temperature : "))
v=round(13.12+0.6215*t-11.37*w**0.16+0.3965*t*w**0.16)

print("THE WIND CHILLINDEX IS :", v)
