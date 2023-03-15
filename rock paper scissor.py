import random
user_choice=input("Enter your move{ rock, paper,scissor}:- ")
computer_choice= random.choice(["rock","paper","scissor"])
print(user_choice,computer_choice)
if user_choice==computer_choice:
     print("match tie")
elif user_choice=="rock":
    if computer_choice=="paper":
        print("Paper covers the Rock,>>>>>>>>>>>>> computer wins *_*_*_*_**_*_* ")
    else:
         print("Rock smashes scissor >>>>>>>>>>>>>>> You Won !!!!!!!!!!!!!!")
elif user_choice=="paper":
    if computer_choice=="scissor":
        print("Scissor cuts the Paper,>>>>>>>>>>>>>> Computer Won *_*_*_*_*_*_*")
    else:
         print("Paper covers the Rock,>>>>>>>>>>>>> You Won !!!!!!!!!!!!!!")
elif user_choice=="scissor":
    if computer_choice=="rock":
        print("Rock smashes scissor >>>>>>>>>>>>>>>Computer Won *_*_*_*_*_*_*")
    else:
         print("Scissor cuts the Paper,>>>>>>>>>>>>> You Won !!!!!!!!!!!!!!")
    