import random
print("welcome to the Rabbit GAME ..")
h = input("press Enter to SKIP or (Help) to have the rules of the game: ").capitalize()
if h:
  print("""game rules:
    1. rock beats scissor
    2. paper beats rock
    3. scissor beats paper""")

ch = input("Enter your choice :").capitalize()
ra = random.choice(['Rock','Paper','Scissor'])
print("you chose :"+ch)
print("computer chose :"+ra)
if ch not in ['Rock','Paper','Scissor']:
  print("INVALID CHOICE .. Try again")
elif ra == ch:
  print("Oobs! it's tie, Try again")
elif (
  (ch == "Rock" and ra == "Paper")
  or
  (ch == "Scissor" and ra == "Rock")
  or
  (ch == "Paper" and ra == "Scissor")):
    print("you lost, Try again")
else:
  print("CONGRATS!! you win✨ 🔥")
  
  