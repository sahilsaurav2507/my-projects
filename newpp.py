name= str(input(print("Enter your name:")))
setage = int(input(print("Enter your age:")))
if setage <=0 or setage >= 105:
    print(f"you are not a human")
elif setage <= 18:
    print(f"hey {name},you can't have beer")
else:
    print("sure you can have the beer")