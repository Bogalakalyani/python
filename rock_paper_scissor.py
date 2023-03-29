#rock paper scissors
wish=input('Do you want game? ')
if wish.lower()=='yes':
    print('welcome to the game!')
else:
    quit()

import random
computer_choice=random.randint in range (0,2)

if computer_choice==0:
    computer_choice='rock'
elif computer_choice==1:
    computer_choice='paper'
else:
    computer_choice='scissor'
print(computer_choice)

user_choice=input('rock,paper,scissor?')
if user_choice.lower()=='rock' and computer_choice.lower()=='paper':
    print('computer wins!')
elif user_choice.lower()=='paper' and computer_choice.lower()=='scissor':
    print('computer wins!')
elif user_choice.lower()=='scissor' and computer_choice.lower()=='rock':
    print('computer wins!')
else:
    print('user wins!')