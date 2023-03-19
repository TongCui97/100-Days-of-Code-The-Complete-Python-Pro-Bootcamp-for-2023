#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo
from replit import clear

EASY_LEVEL_DIFF = 10
HARD_LEVEL_DIFF = 5

# make functions to set difficulity
def set_difficulty():
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  if difficulty == 'easy':
    return EASY_LEVEL_DIFF
  else:
    return HARD_LEVEL_DIFF

# compare answer against the actual value
def compare(guess, answer, turns):
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low")
    return turns - 1
  else:
    print(f"You got it! The answer is {answer}.")

def game():
  # starting text
  print("Welcome to the Number Guessing Game!")
  print(logo)
  print("I'm thinking of a number between 1 and 100.")
  # computer choose a number
  answer = random.randint(1, 100)
  # choose difficulty
  turns = set_difficulty()
  # Let user guess a number
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    turns = compare(guess, answer, turns)
    if turns == 0:
      print("You've run out of guessed, You lose!")
      return
    elif guess != answer:
      print("Guess again.")

game()
run_again = input("This repl has exited, run again? ").lower()
if run_again == 'yes':
  clear()
  game()
    
