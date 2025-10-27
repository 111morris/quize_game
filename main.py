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


# Local Questions by Category

LOCAL_QUESTIONS = {
    "tech": [
        {"question": "What does CPU stand for?", "answer": "central processing unit"},
        {"question": "What does GPU stand for?", "answer": "graphics processing unit"},
        {"question": "What does RAM stand for?", "answer": "random access memory"},
        {"question": "What does API stand for?", "answer": "application programming interface"},
        {"question": "What data structure uses FIFO order?", "answer": "queue"},
        {"question": "What data structure uses LIFO order?", "answer": "stack"},
        {"question": "Which language is used for web styling?", "answer": "css"},
        {"question": "Who developed the Python language?", "answer": "guido van rossum"},
    ],
    "science": [
        {"question": "What is the chemical symbol for water?", "answer": "h2o"},
        {"question": "What planet is known as the Red Planet?", "answer": "mars"},
        {"question": "What gas do plants absorb during photosynthesis?", "answer": "carbon dioxide"},
        {"question": "What is the hardest natural substance on Earth?", "answer": "diamond"},
        {"question": "What part of the cell contains DNA?", "answer": "nucleus"},
    ],
    "geography": [
        {"question": "What is the capital city of Kenya?", "answer": "nairobi"},
        {"question": "Which is the largest continent?", "answer": "asia"},
        {"question": "What river flows through Egypt?", "answer": "nile"},
        {"question": "What is the smallest country in the world?", "answer": "vatican city"},
        {"question": "Mount Everest is located in which mountain range?", "answer": "himalayas"},
    ],
    "general knowledge": [
        {"question": "Who painted the Mona Lisa?", "answer": "leonardo da vinci"},
        {"question": "How many continents are there?", "answer": "7"},
        {"question": "What is the largest ocean on Earth?", "answer": "pacific ocean"},
        {"question": "What is the currency of Japan?", "answer": "yen"},
        {"question": "What year did World War II end?", "answer": "1945"},
    ],
    "health": [
        {"question": "What organ pumps blood through the body?", "answer": "heart"},
        {"question": "How many bones does an adult human have?", "answer": "206"},
        {"question": "What vitamin do you get from sunlight?", "answer": "vitamin d"},
        {"question": "What is the largest organ in the human body?", "answer": "skin"},
        {"question": "What disease is caused by the deficiency of insulin?", "answer": "diabetes"},
    ]
}


# Online Question Fetcher

CATEGORY_MAP = {
    "general knowledge": 9,
    "science": 17,  # Science & Nature
    "geography": 22,
    "tech": 18,  # Science: Computers
    "health": 27,  # Animals or could represent health trivia
}


def fetch_questions_online(amount=5, difficulty="medium", category_name=None):
    """Fetch questions from Open Trivia DB API."""
    base_url = "https://opentdb.com/api.php"
    params = {"amount": amount, "type": "multiple", "difficulty": difficulty}

    if category_name and category_name.lower() in CATEGORY_MAP:
        params["category"] = CATEGORY_MAP[category_name.lower()]

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


# Gameplay

def play_quiz(questions):
    """Main quiz loop."""
    score = 0
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}/{len(questions)}")
        print("-" * 60)
        print(q["question"])

        if "options" in q:  # Multiple choice (from API)
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
        else:  # Free text (local questions)
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
    print("=" * 60)
    print(f"You got {score}/{len(questions)} correct ({percent}%).")

    if percent == 100:
        print("Perfect score! You're a genius!")
    elif percent >= 70:
        print("Great job!")
    elif percent >= 50:
        print("Not bad — keep practicing!")
    else:
        print("Better luck next time!")


# Menu System

def select_category():
    """Let the user pick a quiz category."""
    print("\nAvailable Categories:")
    for i, cat in enumerate(LOCAL_QUESTIONS.keys(), 1):
        print(f"{i}. {cat.title()}")

    choice = ask_int("Select a category number: ", 1, len(LOCAL_QUESTIONS))
    category = list(LOCAL_QUESTIONS.keys())[choice - 1]
    return category


def main():
    slow_print("Welcome to the Ultimate Knowledge Quiz!\n")

    if input("Do you want to play? (yes/no): ").strip().lower() != "yes":
        print("Goodbye!")
        sys.exit()

    while True:
        print("\n=== MAIN MENU ===")
        print("1. Play with Local Questions")
        print("2. Play with Online Questions")
        print("3. Quit")
        choice = input("Select an option (1-3): ").strip()

        if choice == "1":
            category = select_category()
            all_questions = LOCAL_QUESTIONS[category]
            random.shuffle(all_questions)
            num = min(ask_int("How many questions do you want? ", 1, len(all_questions)), len(all_questions))
            play_quiz(all_questions[:num])

        elif choice == "2":
            category = select_category()
            num = ask_int("How many questions (max 10)? ", 1, 10)
            diff = input("Choose difficulty (easy/medium/hard): ").strip().lower()
            questions = fetch_questions_online(num, diff, category)
            if questions:
                play_quiz(questions)
            else:
                print("Could not load questions from the internet.")

        elif choice == "3":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice, try again.")

        replay = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if replay != "yes":
            print("Goodbye, quiz master!")
            break


if __name__ == "__main__":
    main()
