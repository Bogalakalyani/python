
#start
#ask the user that he is intrested in playing
#if he types yes then start the game
#take the random function to generate the random numbers
#ask the user to enter the maximum number with the given random numbers
#if user enter the correct answer then print congratulations you own the game
#if user enter the wrong answer then print sorry you loose the game


print('welcome to Game!')
opinion=input('Are you intrested in playing: ')
if opinion=="yes":
  print('welcome to the game!' )
else: 
  quit()
import random
old_num=[random.randrange(0,9) for value in range(0,4)]
print(old_num)
old_num.sort(reverse=True)
user_ans=input('enter the highest value with above numbers: ')
user_ans_new=list(map(int,user_ans))
if old_num==user_ans_new:
  print('You are right!')
  print('congratulations!,you own the game.')
else:
  print('sorry you loose the game!')
  print('better luck next time')




