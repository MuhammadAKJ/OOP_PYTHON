"""Flight formation"""
from drone import Drone

def create_formation(coordinates):
    """Helper function to create drones at given coordinates."""
    for index, (x, y, z) in enumerate(coordinates, start=1):
        Drone(f'drone{index}', x, y, z)
    print("Drones created:", Drone.all_drones)

def formation_one(x: int, y: int, z: int):
    """Create one drone formation"""
    create_formation([(x, y, z)])

def formation_two(x: int, y: int, z: int, spacing: int):
    """Create two drone formation"""
    create_formation([(x, y, z), (x, y + spacing, z)])

def formation_three(x: int, y: int, z: int, spacing: int):
    """Create three drone formation"""
    create_formation([(x, y, z), (x - spacing, y + spacing, z), (x + spacing, y + spacing, z)])

def formation_four(x: int, y: int, z: int, spacing: int):
    """Create four drone formations"""
    create_formation([(x, y, z), (x, y+spacing, z), (x+spacing, y, z), (x+spacing, y+spacing, z)])

def formation_five(x: int, y: int, z: int, spacing: int):
    """Create five drone formation"""
    create_formation([(x, y, z), (x, y+spacing, z), (x, y-spacing, z), (x+spacing, y, z), (x-spacing, y, z)])

def formation_six(x: int, y: int, z: int, spacing: int):
    """Create six drone formation"""
    create_formation([(x, y, z), (x, y-spacing, z), (x-spacing, y, z), (x+spacing, y, z), (x-(0.5*spacing), y + spacing, z), (x + (0.5*spacing), y + spacing, z)])
