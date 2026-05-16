Task = input("enter the Tasks of Today: ").split(", ")
done = []
undone = []
for x in Task:
  print(x)
  check = input(f"\ndid u finish {x}? (yes-no)\n").lower()
  if check == "yes":
    print("Nice job")
    done.append(Task)
  else:
    print("try not to put it off")
    undone.append(Task)
  print('-------\n')
prog = input("U want to see your progress of the day? (yes-no)\n").lower()
if prog == "yes":
    print(f"""\n****** Done Tasks ******
    {done}
    ****** Ongoing Tasks ******
    {undone}""")
else:
    print("Ok")
    