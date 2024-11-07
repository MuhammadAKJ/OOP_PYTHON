import time
from drone import Drone

def move(direction: str, distance: int, delay: float = 1.0):
    if direction not in ('x', 'y'):
        raise ValueError("Direction must be 'x' or 'y'")
    
    for step in range(1, distance + 1):
        for drone in Drone.all_drones:
            x, y = drone.coordinates
            if direction == 'x':
                drone.coordinates = (x + step, y)
            else:
                drone.coordinates = (x, y + step)
        time.sleep(delay)
    print("Updated drone coordinates:", [drone.coordinates for drone in Drone.all_drones])

if __name__ == "__main__":
    move('x', 20, delay=0.5)
