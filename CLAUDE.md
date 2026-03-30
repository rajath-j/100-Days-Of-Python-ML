# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a "100 Days of Python & AI/ML Challenge" learning repository. It contains standalone Python CLI scripts representing daily exercises/building projects. Each task file is self-contained with educational comments explaining the code concepts.

## Code Architecture

- **Single-file structure**: Each day's work is a separate Python file (task1_age.py, task2_discount.py, etc.) located in the repository root
- **No shared modules**: Files are independent; no imports between tasks or package structure
- **Educational pattern**: Code includes inline comments numbered as steps (e.g., "# 1.", "# 2.") explaining the logic flow - follow this convention when adding new tasks
- **CLI interactive**: All programs use `input()` and `print()` for user interaction. Scripts run until the user chooses to exit or completes the task.
- **No dependencies**: Standard library only (Python 3.x) - no external packages, requirements.txt, or virtual environment

## Learning Progression

Tasks follow a deliberate curriculum progression:
- Day 1-2: Basics (variables, type casting, conditionals)
- Day 3: Loops and control flow
- Day 4: Functions and data structures (lists)
- Day 5: Dictionaries and CRUD operations
- Future days: Will introduce libraries (NumPy, Pandas, etc.) for Data Science/ML

Each task file is self-documenting with educational comments. The README.md should be updated after completing a day's task to reflect the new project.

## Current Tasks (by day)

- **Day 1** (task1_age.py): Age calculator - demonstrates type casting from string to int
- **Day 2** (task2_discount.py): Discount calculator - uses if/elif/else conditionals with float arithmetic
- **Day 3** (task3_guessing_game.py): Guessing game - while loops, break statements, comparison logic
- **Day 4** (task4_todo_list.py): Todo list manager - lists, functions, menu loop
- **Day 5** (task5_contact_book.py): Contact book - dictionaries, CRUD operations, menu-driven interface

## Git & GitHub Workflow

This repository uses Git for version control with a simple workflow:
- Main branch: `main`
- Remote: `origin` (https://github.com/rajath-j/100-Days-Of-Python-ML.git)

**Common commands:**
```bash
# Check status of changes
git status

# View uncommitted changes
git diff

# Stage a specific file
git add taskX_filename.py

# Stage all changes
git add .

# Commit changes (with a clear message describing the day/task)
git commit -m "Day X: Description of completed task"

# Push to GitHub
git push origin main

# Pull latest changes
git pull origin main
```

Note: Always review changes with `git status` and `git diff` before committing. Commits typically represent completion of a day's task.

## Running Code

There are no build, lint, or test commands configured.

To run any task:
```bash
python taskX_filename.py
```

Example:
```bash
python task3_guessing_game.py
```

## Development Notes

- **Python version**: Python 3.x (code uses basic features compatible with 3.6+). Verify with `python3 --version`.
- **No testing framework**: Manual testing by running the script. No pytest/unittest configured.
- **File naming**: New tasks follow the pattern `taskN_description.py` where N is the day number. Keep files in the repository root unless archiving old tasks.
- **README updates**: After completing a task, update README.md to add it to the "Daily Log" section with a brief description of the concept learned.
- **Code style**: Follow the existing educational pattern:
  - Include step comments (e.g., `# 1. Create an empty list`)
  - Use simple, readable code with clear variable names
  - Add inline comments for non-obvious logic
  - Simple error handling appears in later tasks (e.g., checking empty lists/dicts before iteration)
- **Git workflow**: Each day's completion is committed and pushed. Conventional commits like "Day X: Description" are used.
- **No virtual environment**: The project does not use venv/conda; all dependencies are in Python standard library.
