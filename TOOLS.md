# Tools Directory

This file catalogs helper tools available in this repo. Use these as the starting point whenever you need to run common tasks.

- Tool: `tools/create_todays_tasks.py`
  - Purpose: Creates a new folder named `todaysTasks_XXXXXX_YYYY-MM-DD` in the current directory, with an incrementing 6-digit sequence and today’s date.
  - Run (Python): `python tools/create_todays_tasks.py`
  - Output: Prints the absolute path of the created folder and adds a `README.md` inside it.

- Tool: `create-todays-tasks.bat`
  - Purpose: Simple Windows wrapper to run the above Python tool.
  - Run (Windows): Double-click the `.bat` file or run `create-todays-tasks.bat` in a terminal.

Notes:
- These tools operate in the current working directory. Run them from the repo root unless you intentionally want folders elsewhere.
- If `python` isn’t on PATH, the `.bat` wrapper tries `py -3`.
