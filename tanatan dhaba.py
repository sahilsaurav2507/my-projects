logo='''    __
 __ {_/ 
 \_}\\ _
    _\(_)_
   (_)_)(_)_
  (_)(_)_)(_)
   (_)(_))_)  ____
    (_(_(_)  |    |  ____
     (_)_)   |~~~~| |    |
      (_)    '-..-' |~~~~|
               ||   '-..-'
              _||_    ||
             `""""`  _||_
                    `""""`'''
print("...............WELCOME TO TANATAN DHABA..............")
print(logo)
print("---------------------------------------------------")
print("______________________Menu ________________________")
print("chai=10"+"\n"+"coffee=20"+"\n"+"paratha=20"+"\n"+"samosa=10"+"\n"+"poha=15"+"\n"+"kachori=10")
print("..................................................................s")
choice=input("what do you wants to order sir: ")
bill=0
if choice=="chai":
     bill= bill+10
     option=input("do you need extra sugar sir:")
     if option=="yes":
         bill=bill+2
elif choice=="coffee":
     bill= bill+20
     option=input("do you need extra sugar sir:")
     if option=="yes":
         bill=bill+2
elif choice=="paratha":
     bill= bill+20
     option=input("do you need extra sabji sir:")
     if option=="yes":
         bill=bill+10
elif choice=="samosa":
     bill= bill+10
     option=input("do you need extra chatni sir:")
     if option=="yes":
         bill=bill+2
elif choice=="poha":
     bill= bill+15
     option=input("do you need extra onion sir:")
     if option=="yes":
          bill=bill+5
elif choice=="kachori":
     bill= bill+10
     option=input("do you need extra chatni sir:")
     if option=="yes":
         bill=bill+2
print("your total bill = "+str(bill)+ "\t"+ ",thank you ")   