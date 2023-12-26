


principal = int(input("enter principal:"))
rate = int(input("enter rate{per year}:"))
time = int(input("enter time {in years}:"))
SI = ( principal * rate * time )/100
total_amount = SI + principal
print("your simple interest is +" + str(SI) )
print("your total amount is +" + str(total_amount))