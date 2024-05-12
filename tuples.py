t1=(2,3,4,5,6,7,8,9)
val=int(input("enter number(0-7): "))
if val>=0 and val<=7:
    print("value on index number",val,"is: ",t1[val])
else:
    print("invalid")