"""Main File to simulate drone"""
import time
from formation import formation_five
from drone import Drone

def move(direction: str, distance: int, delay: float = 1.0):
    """(function) move
    This function simulate drones movement in the specify x-y axis/direction

    (usage) example
    move(direction = 'x', distance = 20, delay = 1.0)
    
    direction can either be 'x' or 'y'

    distance is an integer value

    delay is a float parameter to simulate time speed
    """
    if direction not in ('x', 'y', 'z'):
        raise ValueError("Direction must be 'x' or 'y' or 'z'")
    
    for step in range(1, distance + 1):
        for drone in Drone.all_drones:
            x, y, z = drone.coordinates
            if direction == 'x':
                drone.coordinates = (x + 1, y, z)
            elif direction == 'y':
                drone.coordinates = (x, y + 1, z)
            else:
                drone.coordinates = (x, y, z + 1)
        print("Updated drone coordinates:", [drone.coordinates for drone in Drone.all_drones])
        time.sleep(delay)
    
def main():
    """Main function"""
    formation_five(34, 24, 10, 5)
    
    move('z', 20, delay=1.5)


if __name__ == "__main__":
    main()    