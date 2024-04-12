print("\n")
print("Welcome to my computer quize")


print("\n\n")
playing = input("Do you want to play the Quize game? ")
print("\n")
if playing.lower() != "yes":
 print("Thanks for your time.")
 quit()
print("Okey! Let's play.\n\nIf you want to quite the game type \"quite\n\n")
score=0

# ============= question one===========

answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit":
 print("Correct!")
 score +=1
 print("\n\n")
elif answer.lower() == "quite":
 print("\n\n")
 print("so sad to see you leave :( ")
 quit()
elif answer.lower() == "q":
 print("\n\n")
 print("so sad to see you leave :( ")
 quit()


else:
 print("incorect!")
 print("\n\n")

# ============= question two===========

answer = input("What does GPU stands for? ")
if answer.lower() == "graphics processing unit":
 print("Correct!")
 score +=1
 print("\n\n")
elif answer.lower() == "quite":
 print("\n\n")
 print("so sad to see you leave :( ")
 quit()
elif answer.lower() == "q":
 print("\n\n")
 print("so sad to see you leave :( ")
 quit()


else:
 print("incorect!")
 print("\n\n")

# ============= question three===========

answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
 print("Correct!")
 score +=1
 print("\n\n")
elif answer.lower() == "quite":
 print("\n\n")
 print("so sad to see you leave :( ")
 quit()
elif answer.lower() == "q":
 print("\n\n")
 print("so sad to see you leave :( ")
 quit()


else:
 print("incorect!")
 print("\n\n")

# ============= question four===========
answer = input("What does UPS stands for? ")
if answer.lower() == "uninterruptable power supply":
 print("Correct!")
 score +=1
 print("\n\n")
elif answer.lower() == "quite":
 print("\n\n")
 print("so sad to see you leave :( ")
 quit()
elif answer.lower() == "q":
 print("\n\n")
 print("so sad to see you leave :( ")
 quit()


else:
 print("incorect!")
 print("\n\n")

# ============= question five===========
answer = input("What does KyU stands for? ")
if answer.lower() == "kirinyaga university":
 print("Correct!")
 score +=1
 print("\n\n")
elif answer.lower() == "quite":
 print("\n\n")
 print("so sad to see you leave :( ")
 quit()
elif answer.lower() == "q":
 print("\n\n")
 print("so sad to see you leave :( ")
 quit()


else:
 print("incorect!")
 print("\n\n")


# ============= question six===========

answer = input("what does UoN stands for? ")
if answer.lower() == "university of nairobi":
 print("Correct!")
 score +=1
 print("\n\n")
elif answer.lower() == "quite":
 print("\n\n")
 print("so sad to see you leave :( ")
 quit()
elif answer.lower() == "q":
 print("\n\n")
 print("so sad to see you leave :( ")
 quit()


else:
 print("incorect!")
 print("\n\n")



# ============= question seven===========
answer = input("The meaning of TUM? ")
if answer.lower() == "technical university of mombasa":
 print("correct!")
 score +1
 print("\n\n")
elif answer.lower() == "quite":
 print("\n\n")
 print("so sad to see you leave :( ")
 quit()
elif answer.lower() == "q":
 print("\n\n")
 print("so sad to see you leave :( ")
 quit()


else:
 print("incorect!")
 print("\n\n")
 
 
 # ============= question 8===========
answer = input("Who is 'mtoza ushuru' in Kenya? ")
if answer.lower() == "ruto":
 print("correct!")
 score +1
 print("\n\n")
elif answer.lower() == "quite":
 print("\n\n")
 print("so sad to see you leave :( ")
 quit()
elif answer.lower() == "q":
 print("\n\n")
 print("so sad to see you leave :( ")
 quit()


else:
 print("incorect!")
 print("\n\n")
 
print("you have got " + str(round((score/8)*100)) + "% of the questions correctly!" )
 