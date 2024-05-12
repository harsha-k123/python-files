list=[120,23,450,-20,11,98,-71]
num=int(input("enter a number: "))
for i in range(len(list)):
    if num==list[i]:
        print("Number is on: ",i)
        break
    else:
        print("Number not in the list")