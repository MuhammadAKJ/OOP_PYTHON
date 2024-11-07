"""Flight formation"""
from drone import Drone

def create_formation(coordinates):
    """Helper function to create drones at given coordinates."""
    for index, (x, y) in enumerate(coordinates, start=1):
        Drone(f'drone{index}', x, y)
    print("Drones created:", Drone.all_drones)

def formation_one(x: int, y: int):
    """Create one drone formation"""
    create_formation([(x, y)])

def formation_two(x: int, y: int, spacing: int):
    """Create two drone formation"""
    create_formation([(x, y), (x, y + spacing)])

def formation_three(x: int, y: int, spacing: int):
    """Create three drone formation"""
    create_formation([(x, y), (x - spacing, y + spacing), (x + spacing, y + spacing)])

def formation_four(x: int, y: int, spacing: int):
    """Create four drone formations"""
    create_formation([(x,y), (x, y+spacing), (x+spacing, y), (x+spacing, y+spacing)])

def formation_five(x: int, y: int, spacing: int):
    """Create five drone formation"""
    create_formation([(x,y), (x, y+spacing), (x, y-spacing), (x+spacing, y), (x-spacing, y)])

def formation_six(x: int, y: int, spacing: int):
    """Create six drone formation"""
    create_formation([(x,y), (x, y-spacing), (x-spacing,y), (x+spacing,y), (x-(0.5*spacing), y+spacing), (x+(0.5*spacing), y+spacing)])
