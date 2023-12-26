import dicecode
import os
while True:
    user_input = int(input("Enter Number of Dice: "))
    if user_input == 0:
       break
dicecode.get_dice(user_input)

