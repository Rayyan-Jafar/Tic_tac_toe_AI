# Tic Tac Toe Game: Strategy Comparison Using Minimax Variants

This project explores how different implementations of the Minimax algorithm affect the performance and decision-making of a simple Tic Tac Toe game.

The game is implemented in Python and offers four strategic approaches for the AI opponent. Alongside the game, a comparison report is provided to evaluate how each approach performs under various criteria.

---

## Project Objectives

- Understand and implement the Minimax algorithm in a game setting
- Compare multiple enhancements of Minimax, including pruning and heuristics
- Evaluate the trade-offs between accuracy and efficiency
- Provide a playable command-line version of Tic Tac Toe

---

## Implemented Strategies

### 1. Minimax (Basic)
- Explores the entire game tree exhaustively
- Guarantees the best move assuming optimal play
- Slower due to deep recursive calls

### 2. Minimax with Heuristic
- Uses a scoring function to evaluate non-terminal game states
- Search is limited to a certain depth
- Faster but may sacrifice perfect accuracy in some situations

### 3. Minimax with Alpha-Beta Pruning
- Skips evaluating unnecessary branches of the tree
- Reduces the number of recursive calls significantly
- Still guarantees the optimal move

### 4. Minimax with Alpha-Beta Pruning and Heuristic
- Combines both optimization techniques
- Balanced approach: fast and reasonably accurate
- Ideal for larger search spaces or real-time play

---

## How to Run the Game

1. Clone the repository:
```bash
git clone https://github.com/your-username/tic-tac-toe-strategies.git
cd tic-tac-toe-strategies
