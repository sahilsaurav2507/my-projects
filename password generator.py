import random

symbol_length =int(input('enter number of symbols:'))
digit_length =int(input('enter number of digits:'))
letter_length =int(input('enter number of letters:'))


letters =['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
digits =[1,2,3,4,5,6,7,8,9,0]
symbols =['!','@','#','$','%','&','*']
if letter_length+digit_length+symbol_length >16:
    print("you can choose only 16 chacracters in your password maximum")
    exit()

password_list=[]

for p in range(0,letter_length):
    password_list.append(random.choice(letters))

for p in range(0,symbol_length):
    password_list.append(random.choice(symbols))

for p in range(0,digit_length):
    password_list.append(random.choice(digits))

random.shuffle(password_list)
password=''

for charater  in password_list:
    password= password+ str(charater)

print(f"your password is:{password}")