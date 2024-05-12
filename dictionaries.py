d1={1:"mon",2:"tues",3:"wed",4:"thurs",5:"fri",6:"sat",7:"sun"}
num=int(input("enter number(1-7): "))
if num>=1 and num<=7:
    print(d1[num])
else:
    print("invalid")