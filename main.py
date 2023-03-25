from art import logo, vs
from game_data import data
from replit import clear
import random
 
# generate information about the celebrate
def information(person):
  person_name = person['name']
  person_description = person['description']
  person_country = person['country']
  return f"{person_name}, a {person_description}, from {person_country}."

# check if the guess is correct, or not
def check_guess(follower1, follower2, choice):
  if follower1 > follower2:
    return choice == 'A'
  else:
    return choice == 'B'

# print logo
print(logo)

# generate 2nd celebrate
person2 = random.choice(data)

game_continue = True
score = 0
while game_continue:
  # Generate celebrate A and B
  person1 = person2
  person2 = random.choice(data)
  while person1 == person2:
    person2 = random.choice(data)
  print(f"compare A: {information(person1)}")
  print(vs)
  print(f"Against B: {information(person2)}")
  # Your guess
  choice = input("Who has more followers? Type 'A' or 'B': ").upper()
  # Record number of follower
  follower1 = person1['follower_count']
  follower2 = person2['follower_count']
  # to see if your guess is correct or not
  is_guess_correct = check_guess(follower1, follower2, choice)
  print(is_guess_correct)
  clear()
  if not is_guess_correct:
    game_continue = False
    print(f"Sorry, that's wrong. Final score: {score}")
  else:
    score += 1
    print(f"You are right! Current score: {score}.")
    

  









