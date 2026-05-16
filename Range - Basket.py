print("*** welcome to ishop calculator ***\n")
basket = int(input("how many items are there in your basket?"))
print(f"\n Let's get to counting them")
bas = []
price = []
for x in range(0,basket):
    item = input(f"please tell me the item of number {x + 1}:")
    bas.append(item)
    pri = float (input(f"plese tell me the price of {item} :\n$"))
    price.append(pri)
all_bas = input("would you like to see the entire basket?").lower()
if all_bas == "yes":
    print(bas)
    all_pri = input("would you like to see how much does it cost you? ").lower()
    if all_pri == "yes":
        print("the total is: ")
    print(sum(price))
else:
    print("ok have a NICE day!")

    
