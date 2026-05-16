print("welcome to multiplication table: ")
number = int(input("Enter any Number: "))
print(f"here is the table of {number}")
for i in range(1,11):
    result = i*number
    print(f"{number} X {i} = {result}")