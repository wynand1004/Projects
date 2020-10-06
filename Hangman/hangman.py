# Hangman (Simple Version)
# by TokyoEdTech
# Python 3.8

import os
os.system("clear")
import random

# Initialize 

words = ["UBUNTU", "PYTHON", "TOKYOEDTECH", "GEANY"]

word = random.choice(words)
guess = "-" * len(word)
wrong_letters = ""

# Print header
print("HANGMAN\n")

print("""
-------
|     
|    
|    
|    
|
|---------""")

# Main game loop
while True:
    print(f"Current Guess: {guess}")
    print(f"Wrong Guesses: {wrong_letters}")
    
    letter = input("\nPlease enter a letter. > ").upper()
    
    # Check if the letter is in the word
    if letter in word:
        temp = ""
        for index in range(len(word)):
            if letter == word[index]:
                temp += letter
            elif guess[index] != "-":
                temp += guess[index]
            else:
                temp += "-"
        guess = temp
                
    else:
        wrong_letters += letter
        
        
    # Check for a winner
    if word == guess:
        print("You win! And you live to play another day!")
        print("""
     O
    \\|/
     |
    / \\""")
        exit()

    # Print the hangman

    if len(wrong_letters) == 0:
        print("""
-------
|     
|    
|    
|    
|
|---------""")

    if len(wrong_letters) == 1:
        print("""
-------
|     O
|    
|    
|    
|
|---------""")

    if len(wrong_letters) == 2:
        print("""
-------
|     O
|     |
|     |
|    
|
|---------""")

    if len(wrong_letters) == 3:
        print("""
-------
|     O
|    \\|/
|     |
|    
|
|---------""")

    if len(wrong_letters) == 4:
        print("""
-------
|     O
|    \\|/
|     |
|    / \\
|
|---------""")
    
    if len(wrong_letters) == 5:
        print("""
-------
|     |
|     O
|    /|\\
|     |
|    | |
|---------""")

    # Check for a loser
    if len(wrong_letters) == 5:
        print("You lose! Sorry sucker!")
        print(f"The word was {word}")
        exit()
