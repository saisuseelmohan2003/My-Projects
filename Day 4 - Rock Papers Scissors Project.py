rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Let's Play Rock Papers Scissors Game !!!")
print("Do you wanna play for best of 3/5/7 ?")
best= int(input())
user_score = 0
computer_score = 0
print("Enter 0 for 'Rock', 1 for 'Paper', 2 for 'Scissors'")
import random
computer_score = 0
user_score = 0
l1=[0,1,2] #user choice
l2=[0,1,2] #computer choice
for i in range(best):
  user_choice = int(input(""))
  if user_choice == 0:
    print(rock)
  elif user_choice == 1:
    print(paper)
  elif user_choice == 2:
    print(scissors)
  computer_choice = random.choice(l2)
  if computer_choice == 0:
    print(rock)
  elif computer_choice == 1:
    print(paper)
  elif computer_choice == 2:
    print(scissors)
  if computer_choice == user_choice:
    print(f"Your Score - {user_score}")
    print(f"Computer Score - {computer_score}")
  elif computer_choice == (user_choice+2 or user_choice-1):
    user_score+=1
    print(f"Your Score - {user_score}")
    print(f"Computer Score - {computer_score}")
  else:
    computer_score+=1
    print(f"Your Score - {user_score}")
    print(f"Computer Score - {computer_score}")
print("Game Over !!!")
if user_score > computer_score:
  print(f"Final Score is  {user_score} - {computer_score}")
  print("You win !!!")
else:
  print(f"Final Score is  {user_score} - {computer_score}")
  print("You lose")
  
