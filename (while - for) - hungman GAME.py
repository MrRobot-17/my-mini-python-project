#Welcome message
import random
from nltk.corpus import words
print(" ... welcome to Hangman GAME! ... ")
word = words.words()
#Variables
random_word = random.choice(word)
brackets = ["_"] * len(random_word)
lives = 7
guessed_letters = []
hangman = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''']
#Asking for letter
help_ = input("press 'ENTER' to skip or 'HELP' to display the rule of the game: ").lower()

if help_ == "help":
    print(''' *** the rules ***
    1. the computer will generate a random word
    2. you have to guess it by guessing a letter form it each time
    3. if the letter right it will be shown in the brackets
    4. if not you will lose a live, if lives finished the game will end 
    * CAREFUL: you only got 7 lives ''')
print("the game start now!")    
print(f"the word contain {len(random_word)} letters")
print(" ".join(brackets))
print('''  +---+
      |
      |
      |
      |
      |
=========''')

while "_" in brackets and lives > 0 :
    user_guess = input("enter you letter (guess): ")
    if user_guess in guessed_letters:
        print("you have already guessed that letter")
        print(f"you still got {lives} lives left")
        continue
    
    guessed_letters.append(user_guess)
    
    for position in range(len(random_word)):
        if random_word[position] == user_guess:
            brackets[position] = user_guess
    print(brackets)
    
    if "_" not in brackets:
        print("you win")
        
    if user_guess not in random_word:
        lives -= 1
        print(hangman[lives])
    print(f"you have {lives} lives left")
if lives == 0:
    print("You lose, better luck next time")
    print(f"the word is ({random_word})")