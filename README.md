# Project Notes and Changelog (Today)

This README tracks all changes made in this folder today. I will append a detailed entry after every change I make.

## How This Works
- Each entry includes a timestamp, a summary, and details.
- Newest entries appear at the top of the changelog.
- If any files are added/updated/removed, they will be listed explicitly.

## Changelog

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
