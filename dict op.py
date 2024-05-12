d1={1:"january",2:"february",3:"march",4:"april",5:"may",6:"june",7:"july",8:"august",9:"september",10:"october",11:"november",12:"december"}
index=int(input("enter index number: "))
if(index<=12 and index>=1):
    print(d1[index])
    del(d1[2])
    print(d1)
    d1[3]="hello"
    print(d1)