print("Welcome to the Computer Quiz!\n")
playing = input("Do you want to play the quiz game? (yes/no) ").strip().lower()
if playing != "yes":
    print("Thanks for your time.")
    quit()

print("\nOkay! Let's play.")
print('If you want to quit the game, type "quit" or "q" at any time.\n')

questions = [
    {"question": "What does CPU stand for?", "answer": "central processing unit"},
    {"question": "What does GPU stand for?", "answer": "graphics processing unit"},
    {"question": "What does RAM stand for?", "answer": "random access memory"},
    {"question": "What does UPS stand for?", "answer": "uninterruptable power supply"},
    {"question": "What does KyU stand for?", "answer": "kirinyaga university"},
    {"question": "What does UoN stand for?", "answer": "university of nairobi"},
    {"question": "The meaning of TUM?", "answer": "technical university of mombasa"},
    {"question": "Who is 'mtoza ushuru' in Kenya?", "answer": "ruto"},
]

score = 0

for q in questions:
    answer = input(q["question"] + " ").strip().lower()
    if answer in ["quit", "q"]:
        print("So sad to see you leave :(")
        quit()
    elif answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")

percent = round((score / len(questions)) * 100)
print(f"You got {score}/{len(questions)} correct. That's {percent}%.")

if percent == 100:
    print("Excellent work!")
elif percent >= 70:
    print("Good job!")
elif percent >= 50:
    print("Not bad, but you can do better.")
else:
    print("Better luck next time!")
