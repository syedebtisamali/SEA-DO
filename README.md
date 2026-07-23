# Study Planner (CLI)

A simple command-line study session tracker written in Python. It walks you through a fixed list of subjects, lets you enter what syllabus you're covering, gives you a suggested time block, and tracks whether you've finished a topic before moving to the next subject.

## Features
- Predefined subject list: Urdu, English, Maths, Physics, Islamiyat, Al-Quran, Computer
- Enter the syllabus/topic you're studying for each subject
- Type `none` to skip a subject and move to the next one
- Shows a suggested time allocation per topic
- Tracks progress with simple commands (`done`, `comp`, `later`) while studying
- Ends automatically once all subjects have been gone through

## Requirements
- Python 3.x
- No external dependencies (uses only the Python standard library)

## Run

```bash
python3 src/main.py
```

## Usage

1. The script prints the list of subjects.
2. For each subject, enter the syllabus/topic you want to study, or type `none` to skip to the next subject.
3. Once you enter a topic, you'll see a suggested time (`10 mins`) to spend on it.
4. While studying, type one of:
   - `done` or `comp` — mark the topic complete and move to the next subject
   - `later` — postpone (a reminder is printed, but you stay on the same topic)
   - anything else — you'll be reminded to continue the current subject
5. The program ends automatically once you've gone through all subjects.

## Project Structure

```
.
├── src/
│   └── main.py       # Main script
├── LICENSE
└── README.md
```

## Known Limitations
- The `while iscompleted := True:` loop condition always evaluates to `True`, so the loop only exits via the internal `break`.
- The suggested time (`req_time`) is a fixed string ("10 mins") and isn't actually enforced with a timer.
- Typing `later` doesn't currently move on or track postponed subjects — it just reprints a reminder.
- No input validation for unexpected characters or empty input.

Contributions and fixes are welcome!

## License
This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
