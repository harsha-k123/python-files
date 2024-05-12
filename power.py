class pow:
    def myPow(self, x, n):
        if n==0:
            return 1
        elif n==1:
            return x
        else:
            return x**n
        
calculate = pow()
result = calculate.myPow(2,2)

print(result)