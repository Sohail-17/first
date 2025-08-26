import random
que = input("Ask the magic 8-ball a question: ") #asks a question to the user
ans = random.randint(1,6)#generates a random number between 1 and 6
if ans ==1: #different outputs for different results
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
while True:#loop to get the user's rating
    rate = input("Are you satisfied with your answer? (only Y or N): ") 
    if rate.lower() == "y":
     print("Good to hear that! ^_^ ")
     break
    elif rate.lower() == "n":
     print("Tuff luck lil bro. ")
     break
    else:
     print("you couldn't follow simple instructions, could you? smh...")
print("Thank you for using the magic 8-ball. Have a nice day! :)")
