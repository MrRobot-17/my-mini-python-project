import random
Tnum = random.randint(0,11)
Gnum = int(input("Enter a number between 1 - 10: "))
while Tnum != Gnum:
    if Gnum > Tnum:
        print("too high, try again with small number")
        Gnum = int(input("enter the number again: "))
    else:
        print("too low, try again with bigger number")
        Gnum = int(input("enter the number again: "))

print(f"that's right the comp choose {Tnum} also")