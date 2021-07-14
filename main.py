#Number Guessing Game Objectives:


import random
import time

guesses_left = 4
is_game_over = False

print("Welcome to the number guesser....I'm thinking about a random number")
for _ in range(3):
    dots = "."
    time.sleep(1)
    print(dots)
    dots += "."

chosen_number = random.randint(1,100)
print(f"debug print {chosen_number}")

players_guess = int(input('Guess a number: '))

while not is_game_over:
    if guesses_left < guesses_left-1:    
        players_guess = int(input(print("Guess againg: ")))
    if players_guess == chosen_number:
        print("MATHAFACKA! YOU WOOOOON")
    elif players_guess > chosen_number:
        print("Puah! I knew you are a mezzacartuccia, go LOWER , MATHAFACKA :))) ")
        guesses_left -=1
        if guesses_left == 0:
            is_game_over = True
            print("You lost MOTHAFAKKA")
            print(f'The number i thought is: {chosen_number}')

    elif players_guess < chosen_number:
        print("Puah! I knew you are a mezzacartuccia, go HIGHER , MATHAFACKA :))) ")
        guesses_left -=1
        if guesses_left == 0:
            is_game_over = True
            print("You lost MOTHAFAKKA")




# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

