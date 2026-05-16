import random
import string
print("welcome to password generator!")
lenght = int(input("enter the lenght of the password : "))
num_letters = int(input("enter num of letters you want :")) 
num_numbers = int(input("enter num of digits you want :")) 
num_sympols = int(input("enter num of sympols you want :"))

letter_str = string.ascii_letters
number_str = string.digits
pun_str = string.punctuation

if lenght != (num_letters + num_numbers + num_sympols):
    print("Invalid Input")
else:
    password = (
        random.choices(letter_str, k=num_letters)+
        random.choices(number_str, k=num_numbers)+
        random.choices(pun_str, k=num_sympols))
random.shuffle(password)
password_join = "".join(password)
print("generated password is: "+password_join)

