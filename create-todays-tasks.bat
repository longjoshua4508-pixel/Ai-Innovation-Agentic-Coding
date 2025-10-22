@echo off
REM Wrapper to create a new todaysTasks_XXXXXX_YYYY-MM-DD folder
REM Usage: double-click or run from shell

setlocal
set SCRIPT_DIR=%~dp0

REM Prefer python if on PATH
python "%SCRIPT_DIR%tools\create_todays_tasks.py" %*
if %ERRORLEVEL% neq 0 (
    echo Attempting to use py launcher...
    py -3 "%SCRIPT_DIR%tools\create_todays_tasks.py" %*
)

endlocal
