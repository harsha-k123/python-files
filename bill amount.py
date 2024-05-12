qty=int(input("enter no. of items sold: "))
val=int(input("enter price of 1 item: "))
disc=int(input("enter discount percent: "))
tax=int(input("enter tax percent: "))
total=qty*val
disc_amt=total*(disc/100)
taxable=total-disc_amt
tax_amt=taxable*(tax/100)
final=taxable*tax_amt
print("final amount is: ",final)

