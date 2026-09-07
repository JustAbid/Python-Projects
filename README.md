# Python Projects – My Learning Journey

This repo is basically a diary of me learning Python.

I started learning Python in December 2025. Instead of just watching tutorials and
forgetting everything the next day, I decided that every time I learn a new concept
I will build a tiny project around it. Nothing fancy – small command line programs
that I can finish in a day or two. This repo is where I keep all of them.

The projects are in the order I built them, so you can kind of see how I went from
"what is a while loop" to putting functions, dictionaries and loops together.

---

## How I work through these

1. Learn a concept (variables, loops, functions, dictionaries, modules...).
2. Think of the smallest possible program that forces me to use it.
3. Build it, break it, fix it.
4. Commit it and write a note here about what clicked for me.

Everything runs with plain Python 3, no external libraries. Just:

```
python <filename>.py
```

---

## The Projects

### 1. Guess the Number — `GuessNumber.py`
*Dec 25, 2025*

My first real program. The computer picks a random number between 1 and 100 and I
keep guessing until I get it. It tells me if my guess is too high or too low, and I
can type `Q` to quit.

**What I learned:**
- Importing and using a module (`random`) for the first time
- `while True` loops and how to stop them with `break`
- Taking input with `input()` and converting it with `int()`
- `if / elif / else` for comparing the guess to the target

### 2. Random Password Generator — `RandomPassGen.py`
*Dec 25, 2025*

Generates an 8 character random password using letters, digits and symbols.

**What I learned:**
- The `string` module (`ascii_letters`, `digits`, `punctuation`) so I don't have to
  type out every character
- `random.choice()` to pick a random item from a sequence
- Building a string piece by piece inside a `for` loop with `+=`

### 3. Text Based Calculator — `calTextBased.py`
*Dec 25, 2025*

A menu driven calculator. Pick an operation (add, subtract, multiply, divide),
enter two numbers, get the answer. It loops until I choose exit.

**What I learned:**
- Writing my own **functions** (`add`, `sub`, `mul`, `div`) and returning values
- Handling the divide by zero case instead of letting the program crash
- Using a menu with a loop so the program keeps running
- `float()` for decimal input, and checking the choice with `if choice in [...]`

### 4. Rock Paper Scissors — `RockPaperGame.py`
*Dec 26, 2025*

Play rock paper scissors against the computer. It checks for invalid input, shows
both choices, decides the winner, and asks if I want to play again.

**What I learned:**
- Validating input by checking against a list (`if userchoice not in validlist`)
- `.lower()` so "Rock", "ROCK" and "rock" all work
- `continue` to skip back to the top of the loop on bad input
- Writing the win condition as one big combined `or` expression

### 5. Simple To-Do List — `todo_list.py`
*Dec 27, 2025*

Add tasks, view them with numbers, delete a task by its number, exit. The tasks
live in a list while the program runs.

**What I learned:**
- Using a **list** to store data and `.append()` / `.pop()` to change it
- `enumerate(tasks, start=1)` to show a numbered list
- f-strings for formatting output (`f"{i}.{addto}"`)
- Checking the number is in range before deleting so it doesn't error

### 6. Contact Book — `contactBook.py`
*Dec 28, 2025*

Add a contact (name + phone), view all contacts, search by name, delete by name.

**What I learned:**
- Using a **dictionary** to store key/value pairs (name → phone number)
- Looping over a dict with `.items()`
- Checking `if name in contactBook` before searching or deleting
- `del` to remove a key
- This one felt like a step up because it mixed dicts, loops and menus together

### 7. Password Strength Checker — `PassStrengthChecker.py`
*Jan 1, 2026*

Type a password and it tells me if it's Weak, Medium or Strong, then gives
suggestions on what to add to make it stronger.

**What I learned:**
- Looping through the characters of a string
- String methods: `.isupper()`, `.islower()`, `.isdigit()`
- Using boolean flags (`has_upper`, `has_digit`...) to track what I've seen
- Combining length + all the flags to decide the strength
- Later I came back and added the suggestions part, so I also learned that a
  project is never really "done"

---

## What's next

I'm still learning. Some things I want to add or build next:
- Save data to a file so the to-do list and contact book don't reset every time
- Error handling with `try / except` (right now typing letters where I expect a
  number still crashes some of these)
- Classes and OOP
- A slightly bigger project that ties a few of these ideas together

## License

MIT — see [LICENSE](LICENSE).
