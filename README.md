# nnei's physics engine

A small **2D soft physics demo** in Python using `pygame`, featuring a player and pushable blocks with different physics behaviors.

## Features

* **Player control**

  * Move with **arrow keys**.
  * Smooth acceleration and friction.

* **Red blocks (soft)**

  * Pushable by the player.
  * Slide with friction and momentum.
  * Collide with each other and static grey blocks.

* **Green blocks (super soft)**

  * Extremely soft and smooth movement.
  * High momentum transfer and low friction.
  * Pushable by the player and other blocks.
  * Interact with red blocks and each other.

* **Grey blocks (static)**

  * Act as solid walls.
  * No block or player can pass through.

* **Soft collision physics**

  * Blocks interact smoothly.
  * Player can push blocks without “flying” forward.
  * Gradual impulse-based collision for natural movement.

## Controls

| Key         | Action            |
| ----------- | ----------------- |
| Arrow Up    | Move player up    |
| Arrow Down  | Move player down  |
| Arrow Left  | Move player left  |
| Arrow Right | Move player right |

## Installation

1. Make sure you have **Python 3.8+** installed.
2. Install `pygame` if not already installed:

```bash
pip install pygame
```

3. Clone or download this repository.

4. Run the game:

```bash
python main.py
```

## How it Works

* The **player and blocks** have velocities.
* Collisions with **static blocks** are resolved to prevent overlap.
* **Soft collisions** between movable blocks transfer momentum gradually.
* **Green blocks** have very low friction → slide smoothly.
* **Red blocks** behave normally → softer than static blocks, but firmer than green blocks.

## Future Improvements

* Add **gravity** and stacking for blocks.
* Implement **sloped surfaces** and ramps.
* Add **jelly-like deformation** for green blocks.
* Sound effects when pushing or colliding.

## License

This project is **CC0** — free to use, modify, and distribute.

Do you want me to do that next?
