# Higher Lower Game Program

'''In this program the user has an option to choose between two popular instagram accounts.  Their goal is to guess which account has more followers.  The game will end once you predict incorrectly.'''

from art import *
from game_data import *
from replit import clear
import random

acc_1 = random.choice(data)
acc_2 = random.choice(data)

if acc_1 == acc_2:
  acc_2 += 1

acc_1_f = acc_1['follower_count']
acc_2_f = acc_2['follower_count']

def play_game(acc_1, acc_2, acc_1_f, acc_2_f, score = 0):

  game_over = False
  while game_over == False:

    print(logo)
  
    if score >= 1:
      print(f"\nThat's correct!  Current score {score}.")
  
    print(f"\nCompare A: {acc_1['name']} a {acc_1['description']} from {acc_1['country']}.")
  
    print(vs)
  
    print(f"\nAgainst B: {acc_2['name']} a {acc_2['description']} from {acc_2['country']}.")
  
    guess = input("\nWho do you think has more followers?  Type 'A' or 'B': ").lower()
  
    if acc_1_f > acc_2_f:
      answer = 'a'
    elif acc_2_f > acc_1_f:
      answer = 'b'
  
    if guess == answer:
      score += 1
      clear()
    elif guess != answer:
      clear()
      print(f"\nSorry, that's not right.  Final score: {score}")
      game_over = True
  
    acc_1 = acc_2
    
    acc_2 = random.choice(data)
    if acc_1 == acc_2:
      acc_2 -= 1

play_game(acc_1, acc_2, acc_1_f, acc_2_f)
  

