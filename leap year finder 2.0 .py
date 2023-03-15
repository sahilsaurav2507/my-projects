year=int(input("Enter your year:"))
if year%400==0 and year%100==0 :
    print("your year is year")
elif year%4==0 and year%100!=0 :
    print("your year is leap year")
else:
    print("your year is not a leap year")