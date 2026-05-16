names = input("Enter First & Second name of your friends separated by comma (,): ").split(", ")
short_names = []
for Q in names:
    Q_split = Q.split()
    print(Q_split)
    
    Fname = Q_split[0]
    Lname = Q_split[1]
    
    Fletter = Fname[0]
    Sletter = Lname[0]
    abbreviation = Fletter + "." + Sletter + "."
    short_names.append(abbreviation)
print("abberative names :")
for x in short_names:
    print(x)