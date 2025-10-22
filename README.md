# Project Notes and Changelog (Today)

This README tracks all changes made in this folder today. I will append a detailed entry after every change I make.

## How This Works
- Each entry includes a timestamp, a summary, and details.
- Newest entries appear at the top of the changelog.
- If any files are added/updated/removed, they will be listed explicitly.

## Changelog

- 2025-10-22 04:03 — Commit updates and attempt GitHub push
  - Created a commit including Resources, tools, flags, and regional structure updates.
  - Commit: 6a3be38 on `main`.
  - Push status: failed from this environment (likely auth/network). Remote `origin` remains configured.
  - Next steps: run `git push -u origin main` locally where you’re authenticated.

- 2025-10-22 03:59 — Add daily tasks folder tool and tools index
  - Added Python script to create a new folder each run using `todaysTasks_XXXXXX_YYYY-MM-DD` naming.
  - Added Windows wrapper `create-todays-tasks.bat` for one-command execution.
  - Added `TOOLS.md` as a living index of helper tools in this repo.
  - Files: `tools/create_todays_tasks.py`, `create-todays-tasks.bat`, `TOOLS.md`.

- 2025-10-22 03:49 — Add OpenAI chatbot docs and summary
  - Created `Resources/` folder with references and a practical summary.
  - Saved:
    - `Resources/openai-node_README.md` (OpenAI Node SDK)
    - `Resources/openai-python_README.md` (OpenAI Python SDK)
    - `Resources/openai_cookbook_streaming.ipynb` (streaming example)
    - `Resources/ChatGPT_Chatbot_Summary.md` (concise how-to for a simple chatbot)
    - `Resources/Official_Doc_Links.txt` (links to official Chat docs)
  - Note: Direct download of platform docs pages was blocked (403); links provided instead.

- 2025-10-22 03:44 — Move flag images into state folders
  - Created `images/` subfolder in each state as needed and moved flags:
    - `united states/South/Arkansas/images/flag.svg`
    - `united states/South/Oklahoma/images/flag.svg`
  - Removed originals from `downloads/` by moving them.

- 2025-10-22 03:42 — Add Arkansas and Oklahoma state flags
  - Created `downloads/` folder and saved flag images from Wikimedia Commons.
  - Files added:
    - `downloads/arkansas-flag.svg`
    - `downloads/oklahoma-flag.svg`
  - Source: Wikimedia Commons (public domain/compatible licenses as provided on the file pages).

- 2025-10-22 03:39 — Group states into regional folders
  - Created region folders under `united states/`: `Northeast`, `Midwest`, `South`, `West`.
  - Moved each state folder into its corresponding region per U.S. Census regions.
  - Example paths: `united states/South/Texas`, `united states/Northeast/New York`, `united states/Midwest/Illinois`, `united states/West/California`.
  - All 50 states organized; existing `info.txt` files moved with their folders.

- 2025-10-22 03:29 — Configure GitHub remote
  - Set `origin` to `https://github.com/longjoshua4508-pixel/Ai-Innovation-Agentic-Coding.git`.
  - Note: Initial push attempted earlier but timed out due to environment network limits. Remote is configured; push when network permits.

- 2025-10-22 03:20 — Completed Git initialization
  - Initialized Git repository on branch `main`, staged all files, and created initial commit.
  - Local Git used: C:\Program Files\Git\cmd\git.exe
  - Latest commit: d4079f0
  - Note: Git may convert LF to CRLF on checkout per Windows defaults.

- 2025-10-22 03:09 — Git initialization deferred (Git not found)
  - Attempted to run `git` commands but `git` is not available on PATH in this environment.
  - Current state: `.gitignore` added, but repository not yet initialized.
  - Next actions: install Git and run the commands listed in the instructions.

- 2025-10-22 03:07 — Initialize Git repository and add .gitignore
  - Added a minimal `.gitignore` for OS/IDE files.
  - Planned: initialize Git, create initial commit, set default branch to `main`.
  - Next step: add GitHub remote and push.

- 2025-10-22 03:01 — Random verification of info.txt files
  - Ran a random spot-check of 9 state `info.txt` files to verify capital names and coordinates (±0.001 tolerance).
  - Report:
    - Alabama: Exists=True; Capital=True; Lat=True; Lon=True
    - West Virginia: Exists=True; Capital=True; Lat=True; Lon=True
    - Minnesota: Exists=True; Capital=True; Lat=True; Lon=True
    - Maine: Exists=True; Capital=True; Lat=True; Lon=True
    - Tennessee: Exists=True; Capital=True; Lat=True; Lon=True
    - Vermont: Exists=True; Capital=True; Lat=True; Lon=True
    - New Jersey: Exists=True; Capital=True; Lat=True; Lon=True
    - Massachusetts: Exists=True; Capital=True; Lat=True; Lon=True
    - Utah: Exists=True; Capital=True; Lat=True; Lon=True
  - Summary: Verified 9 states. Full matches: 9. States checked: Alabama, West Virginia, Minnesota, Maine, Tennessee, Vermont, New Jersey, Massachusetts, Utah

- 2025-10-22 02:58 — Add capital and coordinates info.txt files
  - Added `info.txt` to each state folder under `united states/`.
  - Each file lists: State name, capital city, latitude, and longitude for the capital.
  - Files: added `united states/<State>/info.txt` for all 50 states.

- 2025-10-22 02:51 — Create United States folder structure
  - Created `united states` directory with 50 state subfolders.
  - Details: Alabama, Alaska, Arizona, Arkansas, California, Colorado, Connecticut, Delaware, Florida, Georgia, Hawaii, Idaho, Illinois, Indiana, Iowa, Kansas, Kentucky, Louisiana, Maine, Maryland, Massachusetts, Michigan, Minnesota, Mississippi, Missouri, Montana, Nebraska, Nevada, New Hampshire, New Jersey, New Mexico, New York, North Carolina, North Dakota, Ohio, Oklahoma, Oregon, Pennsylvania, Rhode Island, South Carolina, South Dakota, Tennessee, Texas, Utah, Vermont, Virginia, Washington, West Virginia, Wisconsin, Wyoming.
  - Files: added folder `united states` and 50 subfolders (one per state).

- 2025-10-22 00:00 — Initialize README and changelog
  - Created this `README.md` to record today’s changes.
  - Notes: Added purpose, usage, and changelog structure.
  - Files: added `README.md`
