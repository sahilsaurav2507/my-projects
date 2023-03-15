for s in range(1,101):
    if s % 5==0 and s % 3 ==0:
        print("Fizz buzz") 
    elif s % 5 == 0:
        print("buzz")
    elif s % 3 == 0:
        print("fizz")   
    elif  s % 5!=0 and s % 3 !=0:
        print(s)