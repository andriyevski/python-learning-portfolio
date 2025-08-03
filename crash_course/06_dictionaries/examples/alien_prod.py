from typing import Dict


def alien() -> Dict[str, object]:
    """Create a new alien with initial attributes."""
    return {'color': 'green', 'points' : 5}

def show_color(alien: Dict[str, object]) -> None:
    """Display the alien's color"""
    print(f"Color: {alien['color']}")

def show_points(alien: Dict[str, object]) -> None:
    """Print a message with the alien's point value."""
    new_points = alien['points']
    print(f"You just earned {new_points} points!")

def add_new_param(alien: Dict[str, object], x: int, y: int) -> None:
    """Add position coordinates to the alien."""
    alien['x_position'] = x
    alien['y_position'] = y
    print(f"Show position now: {x}, {y}")

def change_color(alien: Dict[str, object], new_color = str) -> None:
    """Change the alien's color."""
    old_color = alien['color']
    alien['color'] = new_color
    print(f" The alien color changed from {old_color} to new {new_color} color!.")


# === MAIN EXECUTION ===
alien = alien()

show_color(alien)
show_points(alien)

add_new_param(alien, 0, 25)
change_color(alien, 'white')
show_color(alien)
