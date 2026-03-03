# Student Syllabus Tracker

A Python-based CLI (Command Line Interface) tool designed to help students manage their study sessions across multiple subjects. It provides a structured way to track what syllabus needs to be covered and ensures the user stays focused on the current task before moving forward.

## Features

* **Pre-defined Subject List**: Includes core subjects like Urdu, English, Maths, Physics, and Computer Science.
* **Syllabus Input**: Allows you to define exactly what you are studying for each session.
* **Time Management**: Sets a 10-minute focus window per topic.
* **Progress Lock**: Uses a logic loop that prevents moving to the next subject until the current one is marked as "done" or "comp".
* **Skip Logic**: Type "none" for a syllabus if you want to skip that specific subject for the day.

---

## Project Structure

* **main.py**: Contains the primary logic for the study loop, subject navigation, and completion prompts.

---

## How It Works

The script follows a linear study path:
1. It displays the current subject.
2. It asks for the specific syllabus/topic you plan to cover.
3. It starts a "focus mode" where it prompts you for status updates.
4. You must enter **done** or **comp** to successfully move to the next subject in the list.



---

## Usage

### Prerequisites
* Python 3.x installed.

### Execution
Run the script in your terminal:
```bash
python main.py
Commands

Command	Result
none	Skips the current subject.
done / comp	Marks subject as finished and moves to the next.
later	Rebukes the user to stay focused (encouragement mode).
Anything else	Reminds the user to continue the current subject.
Technical Logic
The script utilizes a while loop with a nested boolean toggle (iscompleted).

Data Structure: A list of strings for subjects.

Iteration: A counter-based approach to navigate the list index.

Input Handling: Case-insensitive logic for "none" to handle skips.

Future Roadmap
Custom Timers: Allow the user to input how many minutes they need for a specific topic.

Persistent Storage: Save progress to a file so you can resume studying after closing the program.

Break Reminders: Automatically insert a 5-minute break after every two subjects.
