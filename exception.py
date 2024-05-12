def divide(a,b):
    if b==0:
        raise Exception ("cannot divide by zero!")
    else:
        return a/b
    
try:
    result = divide(10,0)
    print("result: ", result)

except Exception as e:
    print("error: ", str(e))