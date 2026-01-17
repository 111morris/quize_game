# Advanced Python Quiz Game

A fun, category-based quiz game built in Python — supporting both local and online trivia questions!  
Play offline with your own question bank or online using [Open Trivia DB](https://opentdb.com/).

---

## Overview

This is a command-line quiz application where players can test their knowledge across multiple categories:

-  Geography
-  Science
-  Tech & Programming
-  General Knowledge
-  Health

The game includes both local questions and API-powered online questions (with difficulty levels), plus a clean, friendly interface and robust error handling.

---

## Features

| Feature               | Description                                                                               |
|-----------------------|-------------------------------------------------------------------------------------------|
|  Multiple Categories | Choose from Science, Tech, Geography, Health, and General Knowledge                      |
|  Online & Offline Modes | Play with local questions or fetch live ones from Open Trivia DB                    |
|  Difficulty Levels       | Choose easy, medium, or hard in online mode                                     |
|  Menu System            | Simple navigation through modes and categories                                    |
|  Quit Anytime            | Type `q` or `quit` to exit mid-game                                               |
|  Smart Scoring           | Get your results and performance summary                                          |
|  Expandable              | Easily add new question sets or categories                                       |
|  Error Handling          | Handles invalid inputs and API timeouts gracefully                               |
|  User Experience         | Animated intro, emojis, and clear formatting                                      |

---

##  Installation

**1 Clone the repository**
```bash
git clone https://github.com/111morris/quize_game.git
cd quize_game
```


** Install dependencies**

The game uses the `requests` module for fetching online questions.

```bash
pip install requests
```


** Run the game**
```bash 
python3 main.py
```


---

##  How to Play

1. Launch the game:
    ```
    python quiz_game.py
    ```
2. Type `yes` when asked if you want to play.
3. Choose whether you want:
    - Local questions (offline mode)
    - Online questions (fetched from Open Trivia DB)
4. Select your category (Science, Tech, Geography, Health, etc.).
5. (Optional for online mode) Choose difficulty: easy, medium, or hard.
6. Answer each question — type `q` anytime to quit.
7. Get your score, percentage, and feedback at the end!

---

##  Project Structure

```
advanced-quiz-game/
│
├── quiz_game.py # Main game script
├── README.md # Project documentation
├── requirements.txt # Python dependencies (optional)
└── assets/ # Future use (images, sounds, etc.)
```


---

##  Local Question Structure

Local questions are stored in a Python dictionary within the file:

```
LOCAL_QUESTIONS = {
"tech": [
{"question": "What does CPU stand for?", "answer": "central processing unit"},
{"question": "What is FIFO in data structures?", "answer": "queue"},
# ...
],
"science": [
{"question": "What gas do plants absorb?", "answer": "carbon dioxide"},
# ...
],
# ...
}
```


 You can add new categories or questions directly to this dictionary!

---

##  Online Mode

The game fetches live trivia questions using the [Open Trivia DB API](https://opentdb.com/).

Example API call:

```bash
https://opentdb.com/api.php?amount=5&type=multiple&category=18&difficulty=medium
```


The category IDs are automatically mapped:

| Category              | API ID |
|-----------------------|--------|
| General Knowledge     | 9      |
| Science               | 17     |
| Geography             | 22     |
| Tech (Computers)      | 18     |
| Health                | 27     |

---

##  Requirements

- Python 3.8+
- `requests` library

You can install dependencies manually:

```bash
pip instal requests
```

Or add this to `requirements.txt`:

```bash
requests>=2.30.0
```


---

##  Future Enhancements

-  High Score System (save results to a file or database)
-  GUI Version using Tkinter or PyGame
-  Timed Questions for extra challenge
-  Sound Effects or Voice Prompts
-  More Categories & APIs

---


##  Author

Morris Mulandi

 Email: [mulandimorris1@gmail.com](mailto:mulandimorris1@gmail.com)  
 GitHub: [111morris](https://github.com/111morris)

made with ❤️ 
