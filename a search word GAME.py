import random

# جميع المتغيرات
letters = ['B', 'S', 'T', 'R', 'I', 'K', 'E']
words = ['BIKE', 'STRIKE', 'TRIKE', 'BIKES', 'TRIBE', 'RIBE', 'SIKE', 'BITE', 'SITE', 'TRIKES', 'BIT', 'SIT', 'RISE']
guessed_word = []

# الرسالة المعروضة للمستخدم
inst_message = input('''. . . welcome to the "GUESS THE WORD" game . . .
      press (INST) to got the instruction of the game or press "ENTER" to skip it and start the game: ''').lower()

if inst_message == "inst":
    print(''' * * * Here are the rules of the game  * * *
          1. first it will display you a random letters.
          2. and simply you can type as many as word you can get.
          3. press "R" if you wanna shuffle the letters.
          4. press "EXIT" if you think you finished the words.''')

print(letters)

while True:
    guessed = input("Enter a word that might be up in letters: ").upper()
    
    if guessed == "EXIT":
        break
    if guessed == "R":
        random.shuffle(letters)
        print("Shuffled letters:", letters)
        continue

    if guessed in guessed_word:
        print("It already up there, try again.")
        continue

    if guessed in words:
        print(f"The word {guessed} is right, carry on.")
        guessed_word.append(guessed)
    else:
        print("SORRY! it's not in the dictionary.")