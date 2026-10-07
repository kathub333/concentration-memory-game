# Concentration: Memory Card Game

A 2-player memory card game ("Concentration") with a graphical interface, built as a Class XII group project. Players flip two cards at a time to find matching pairs. Scores are tracked live, and winners are saved to a MySQL database to build a leaderboard.

## Features
- 8 pairs of cards, 2 players
- Live score counter and a display showing whose turn it is
- Player name entry with validation (letters only, names cannot be empty)
- Winners (and ties) saved to MySQL
- Leaderboard ranked by number of wins

## Screens
1. Opening window
2. Player input window
3. Memory game window
4. Post-game window
5. Leaderboard window

## Tech
Python, Tkinter, Pillow, MySQL

## How to run
1. Install Python 3 and MySQL Server (make sure it is running)
2. Install dependencies: `pip install -r requirements.txt`
3. Open `main.py` and replace `your_password` with your MySQL root password
4. Keep the card images (`back.png`, `1.png` to `8.png`) in the same folder as `main.py`
5. Run the game: `python main.py`

The `card_game` database and `memory` table are created automatically on first run. You can also create them manually with `setup.sql`.

The leaderboard shows up after at least one game has been finished.

## Database
- Database: `card_game`
- Table: `memory` (`sr_no`, `player1`, `player2`, `winner`)

## My contribution
GUI, game logic, and the project report (team of 3).

## Note
The console prints the card layout when a game starts. This was left in as a debugging aid during development.
