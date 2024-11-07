MAX_X = 1366
MAX_Y = 768
MAX_Z = 100

class Drone:
    """This is a drone class"""
    
    all_drones = []

    def __init__(self, name: str, x: int, y: int, z: int):
        assert 0 <= x < MAX_X, f"x coordinate must be in range (0, {MAX_X})"
        assert 0 <= y < MAX_Y, f"y coordinate must be in range (0, {MAX_Y})"
        assert 0 <= z < MAX_Z, f"z coordinate must be in range (0, {MAX_Z})"
        
        self.__name = name
        self.__x = x
        self.__y = y
        self.__z = z
        Drone.all_drones.append(self)

    @property
    def coordinates(self):
        """Get cordinates"""
        return self.__x, self.__y, self.__z

    @coordinates.setter
    def coordinates(self, new_coordinates):
        x, y, z = new_coordinates
        if not (0 <= x < MAX_X):
            raise ValueError(f"x coordinate must be in range (0, {MAX_X})")
        if not (0 <= y < MAX_Y):
            raise ValueError(f"y coordinate must be in range (0, {MAX_Y})")
        if not (0 <= z < MAX_Z):
            raise ValueError(f"z coordinate must be in range (0, {MAX_Z})")
        self.__x, self.__y, self.__z = x, y, z

    def __repr__(self):
        return f"Drone(name={self.__name}, x={self.__x}, y={self.__y}, z={self.__z})"
    
    def __str__(self):
        return self.__name
