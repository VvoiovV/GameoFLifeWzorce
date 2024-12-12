# Game of Life in Python

---

## Description
This project is an implementation of John Conway's **Game of Life** in Python. The application simulates the evolution of cells on a two-dimensional grid based on predefined rules, allowing the user to observe dynamic patterns emerging during the simulation.

---

## Features
- Initializes a random starting grid of cells.
- Visualizes successive generations in the console.
- Allows customization of the grid size and the number of generations.
- Implements GOL rules: survival, birth, and death of cells.

---

## File Structure
```
GameOfLife/
├── game/
│   ├── __init__.py
│   ├── board.py
│   ├── cell.py
│   └── game.py
├── main.py
└── README.md
```

---

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/VvoiovV/GameoFLifeWzorce.git
   ```
2. Navigate to the project directory:
   ```bash
   cd GameoFLifeWzorce
   ```
3. Install required dependencies if not already installed:
   ```bash
   pip install pygame numpy
   ```
4. Run the application:
   ```bash
   python main.py
   ```

---

## System Requirements
- Python 3.x
- **pygame** library
- **numpy** library

---

## Possible Improvements
- **GUI Integration**: Add a graphical user interface for better visualization.
- **Save and Load States**: Enable saving and loading of game states.
- **Custom Rules**: Allow users to define their own evolution rules.

---

If you have any questions or suggestions about the project, feel free to reach out! 😊
