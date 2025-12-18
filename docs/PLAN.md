# Project Plan

This document outlines the plan for the Clash of Clans Info Bot.
Clash of Clans Info Project – Step‑by‑Step Guide
1. Project overview
Goal v1: Telegram bot written in Python that:

You give it your Supercell player tag (from Clash of Clans).

It calls the Clash of Clans API (using your API key).

It replies with info like your Town Hall level and other player details.

Goal v2: Simple website (HTML/CSS + maybe a tiny Python backend later) that shows similar info in the browser.

2. Prerequisites to install
Create accounts

GitHub account.

Telegram account.

Supercell Developer account for Clash of Clans API (to get an API key).

Install tools

Install Git (so you can push to GitHub).

Install Python 3.x.

Install Visual Studio Code.

Install a browser (Chrome, Firefox, etc.) for website testing.

Recommended VS Code extensions

"Python" (Microsoft).

"GitHub Pull Requests and Issues".

"Live Server" (for the website later).

3. Create the GitHub repository
Go to GitHub and click New repository.

Name it something like:
clash-info-bot
(later you can add another repo or folder for the website version).

Choose:

Public repository.

Check Add a README file.

Choose .gitignore: Python (optional but helpful).

License: MIT (or any you like).

Click Create repository.

On your computer:

Choose a folder where you want to keep projects.

Open a terminal (or Git Bash) and run:

bash
git clone https://github.com/<your-username>/clash-info-bot.git
cd clash-info-bot
Open this folder in VS Code:

File -> Open Folder... and select clash-info-bot.

4. Organize the project structure (v1: Telegram bot)
In VS Code, create this structure:

text
clash-info-bot/
  README.md
  .gitignore
  requirements.txt
  bot/
    __init__.py
    config_example.py
    main.py
    coc_api.py
    telegram_handlers.py
    utils.py