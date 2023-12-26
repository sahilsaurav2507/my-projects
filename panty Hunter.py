
import random 
import sys


row1=['👙','👙','👙']
row2=['👙','👙','👙']
row3=['👙','👙','👙']
map= [row1,row2,row3]
print(f'{row1}\n{row2}\n{row3}')

computer_choice= random.choice([11,12,13,21,22,23,31,32,33])

u_input1= input("Enter your first choice:")
row=int(u_input1[0])-1
column=int(u_input1[1])-1
if u_input1 == computer_choice:
    print('you won!!!')
    map[row][column] = '💋'
    print(f'{row1}\n{row2}\n{row3}')
    sys.exit()

map[row][column]= '🖕'
print(f'{row1}\n{row2}\n{row3}')

u_input1= input('Enter your 2nd choice:')
row=int(u_input1[0])-1
column=int(u_input1[1])-1
if u_input1==computer_choice:
    print('you won!!!')
    map[row][column] = '💋'
    print(f'{row1}\n{row2}\n{row3}')

map[row][column]= '🖕'
print(f'{row1}\n{row2}\n{row3}')


u_input1= input('Enter your 3rd choice:')
row=int(u_input1[0])-1
column=int(u_input1[1])-1
if u_input1==computer_choice:
    print('you won!!!')
    map[row][column] = '💋'
    print(f'{row1}\n{row2}\n{row3}')
map[row][column] = '💋'
print(f'{row1}\n{row2}\n{row3}')


