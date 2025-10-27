import requests
import html
import random
import time
import sys

# Utility Functions

def slow_print(text, delay=0.03):
    """Print text slowly for dramatic effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def ask_int(prompt, min_val=1, max_val=None):
    """Ask for an integer with error handling."""
    while True:
        try:
            val = int(input(prompt))
            if val < min_val:
                print(f"Please enter a number >= {min_val}.")
                continue
            if max_val and val > max_val:
                print(f"Please enter a number <= {max_val}.")
                continue
            return val
        except ValueError:
            print("Invalid number. Try again.")


# Question Sources

def get_local_questions():
    """Return a set of local quiz questions."""
    return [
        {"question": "What does CPU stand for?", "answer": "central processing unit"},
        {"question": "What does GPU stand for?", "answer": "graphics processing unit"},
        {"question": "What does RAM stand for?", "answer": "random access memory"},
        {"question": "What does UPS stand for?", "answer": "uninterruptable power supply"},
        {"question": "What does KyU stand for?", "answer": "kirinyaga university"},
        {"question": "What does UoN stand for?", "answer": "university of nairobi"},
        {"question": "What does TUM stand for?", "answer": "technical university of mombasa"},
        {"question": "Who is 'mtoza ushuru' in Kenya?", "answer": "ruto"},
    ]


def fetch_questions_online(amount=5, difficulty="medium", category=None):
    """Fetch questions from Open Trivia DB API."""
    base_url = "https://opentdb.com/api.php"
    params = {"amount": amount, "type": "multiple", "difficulty": difficulty}
    if category:
        params["category"] = category

    try:
        response = requests.get(base_url, params=params, timeout=5)
        data = response.json()
        if data["response_code"] != 0:
            print("Could not fetch questions. Try again later.")
            return []
        questions = []
        for q in data["results"]:
            question_text = html.unescape(q["question"])
            correct = html.unescape(q["correct_answer"]).lower()
            wrong = [html.unescape(a) for a in q["incorrect_answers"]]
            all_options = wrong + [q["correct_answer"]]
            random.shuffle(all_options)
            questions.append({
                "question": question_text,
                "options": all_options,
                "answer": correct
            })
        return questions
    except Exception as e:
        print(f"Error fetching questions: {e}")
        return []


# Game Logic

def play_quiz(questions):
    """Main quiz loop."""
    score = 0
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}/{len(questions)}")
        print("-" * 50)
        print(q["question"])

        if "options" in q:  # online questions
            for idx, option in enumerate(q["options"], 1):
                print(f"{idx}. {option}")
            user_input = input("Your answer (1-4 or 'q' to quit): ").strip().lower()
            if user_input in ["q", "quit"]:
                print("\nExiting quiz early.")
                break
            if user_input.isdigit() and 1 <= int(user_input) <= len(q["options"]):
                chosen = q["options"][int(user_input) - 1].lower()
            else:
                print("Invalid input.")
                continue
        else:  # local questions (typed answers)
            chosen = input("Your answer: ").strip().lower()
            if chosen in ["q", "quit"]:
                print("\nExiting quiz early.")
                break

        if chosen == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The correct answer was: {q['answer']}\n")

    percent = round((score / len(questions)) * 100)
    print("=" * 50)
    print(f"You got {score}/{len(questions)} correct ({percent}%).")

    if percent == 100:
        print("Perfect score! You're a genius!")
    elif percent >= 70:
        print("Great job!")
    elif percent >= 50:
        print("Not bad — keep practicing!")
    else:
        print("Better luck next time!")


# Game Menu

def main():
    slow_print("🎮 Welcome to the Advanced Computer Quiz!\n")

    play_choice = input("Do you want to play the quiz game? (yes/no): ").strip().lower()
    if play_choice != "yes":
        print("Thanks for your time.")
        sys.exit()

    while True:
        print("\n=== MAIN MENU ===")
        print("1. Play with Local Questions")
        print("2. Play with Online Questions")
        print("3. Quit")
        choice = input("Select an option (1-3): ").strip()

        if choice == "1":
            questions = get_local_questions()
            random.shuffle(questions)
            num = min(ask_int("How many questions do you want? ", 1, len(questions)), len(questions))
            play_quiz(questions[:num])

        elif choice == "2":
            num = ask_int("How many questions do you want (max 10)? ", 1, 10)
            diff = input("Choose difficulty (easy/medium/hard): ").strip().lower()
            questions = fetch_questions_online(num, diff)
            if questions:
                play_quiz(questions)
            else:
                print("Could not load questions from the internet.")

        elif choice == "3":
            print("Goodbye! Thanks for playing.")
            break

        else:
            print("Invalid choice, try again.")

        replay = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if replay != "yes":
            print("See you next time!")
            break


if __name__ == "__main__":
    main()
