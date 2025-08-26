import random
que = input("Ask the magic 8-ball a question: ")
ans = random.randint(1,6)
if ans ==1:
    print("YAAAASSS!")
elif ans == 2:
    print("Gotta work hardf broski.")
elif ans == 3:
    print("Uhh! Maybe something else?")
elif ans == 4:
    print("Nope, not happening. ")
elif ans == 5:
    print("NAAAAAAAAAAAHH!")
else:
    print("GET OUTTTTTA HEREEE!")
while True:
    rate = input("Are you satisfied with your answer? (only Y or N): ")
    if rate.lower() == "y":
     print("Good to hear that! ^_^ ")
     break
    elif rate.lower() == "n":
     print("Tuff luck lil bro. ")
     break
    else:
     print("you couldn't follow simple instructions, could you? smh...")
