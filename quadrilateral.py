class Quad:
    def __init__(self, height: float, weight: float):
        assert height > 0.00, "Height must be greater than zero"
        assert weight > 0.00, "Weight must be greater than zero"

        self.__height = height
        self.__weight = weight

    def perimeter(self):
        return (self.__height + self.__weight) * 2

    @property
    def properties(self):
        return self.__height
    
    @__init__.setter
    def overwrite(self, height, weight):
        self.__height = height
        self.__weight = weight

square = Quad(20,10)
print(square.perimeter())