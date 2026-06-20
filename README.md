##Battleship — Python Terminal Simulator

A fully-featured Battleship game playable in the terminal, built in Python with no external dependencies. Three game modes including an AI vs AI statistical simulation over 100 games.


🎓 Group project (4 people) — L1 Maths-CS, Université Paris Cité. The goal was to reproduce the classic Battleship game as a Python terminal application.




Preview

    1 2 3 4 5 6 7 8 9 10
A   . . . . . . . . . .
B   . . . B B B B . . .
C   . . . . . . . . . .
D   . B . . . . . . . .
E   . B . . . . . . . .
F   . B . . . X . . . .
G   . . . . . . . . . .
H   . . . . . O . . . .
I   . . . . . . . . . .
J   . . . . . . . . . .

Legend:  B = ship  |  X = hit  |  O = miss


Features


3 game modes

1 — Human vs Human (hotseat)
2 — Human vs AI
3 — AI vs AI (statistics over 100 games)



Smart ship placement

5 ships with standard sizes: 5, 4, 3, 3, 2
Overlap and adjacency checks between ships
Directional placement: Z (up) S (down) Q (left) D (right)



AI with targeting logic

Fires randomly until a ship is hit
Then targets adjacent cells to finish off the ship
Automatically marks cells around a sunken ship as useless



Statistics mode (mode 3)

Silently simulates 100 AI vs AI games
Displays each side's win rate
Determines whether the first player has a statistical advantage






Getting Started

Requirements: Python 3.x — no external libraries needed.

bashgit clone https://github.com/your-username/battleship-simulator.git
cd battleship-simulator
python BN1_code.py

Then choose your game mode in the terminal:

Choose your mode: 1 (H vs H)  |  2 (H vs AI)  |  3 (AI vs AI stats)


Project Structure

battleship-simulator/
│
├── BN1_code.py       # Single source file — all game logic
└── README.md


Code Overview

The project follows a functional approach: each responsibility is isolated in a documented function with its type signature.

FunctionRolecreer_grille()Initializes an empty 10×10 gridafficher_grille()Renders the grid in the terminalconvertir_coordonne()Parses and validates user input (e.g. A5)peut_placer_bateau()Checks placement constraints (bounds + adjacency)placer_bateaux()Interactive ship placement for a human playerplacer_bateaux_IA()Random rule-compliant placement for the AIverifier_bateau_coule()Detects whether all cells of a ship have been hittirer()Human player's shooting turntirer_IA()AI shooting turn (smart targeting)partie()Entry point — handles all 3 game modes


What I Learned

This was a first-year group project at Université Paris Cité, built collaboratively with 3 teammates. It helped me work on:


Modeling a game state with separate grids (real state vs display)
Implementing a simple AI combining random fire with a targeting heuristic
User input validation and edge case handling
Writing documented, readable code with docstrings on every function



Possible Improvements


 Advanced AI: probability-based hunt & target algorithm
 Graphical interface using tkinter or pygame
 Save / load game
 Network mode (two players on two machines)
