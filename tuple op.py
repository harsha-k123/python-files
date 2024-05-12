t1=(0,2,4,6,8,10)
print(t1)
index=int(input("enter index number(0-5): "))
if (index>=0 and index<=5):
    print("value at index",index,"is: ",t1[index])
else:
    print("invalid")
l1=list(t1)
update=int(input("enter index number(0-5) to be updated: "))
val=int(input("enter value to be updated: "))
if(update<=5 and update>=0):
    l1[update]=val
else:
    print("invalid")