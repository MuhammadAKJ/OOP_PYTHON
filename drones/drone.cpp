#include <string>
#include <iostream>
#include <cassert>
#include <tuple>
#include <vector>

const int MAX_X = 1366;
const int MAX_Y = 768;
const int MAX_Z = 100;

class AbstractClass{
    virtual void collision() = 0;
};

class Drone: AbstractClass {
private:
    std::string name;
    int x_cor, y_cor, z_cor;

public:
    //Public variables
    std::vector<std::string> *drone_location;
    // Constructor
    Drone(std::string aName, int aX, int aY, int aZ) {
        assert(aX > 0 && aX < MAX_X && "x must be positive and in range");
        assert(aY > 0 && aY < MAX_Y && "y must be positive and in range");
        assert(aZ > 0 && aZ < MAX_Z && "z must be positive and in range");
        name = aName;
        x_cor = aX;
        y_cor = aY;
        z_cor = aZ;
        
    }

    //Collision contract implementation
    void collision(){

    }

    //Get coordinates and return tuples
    std::tuple<int, int, int> getCordinates() {
        return std::make_tuple(x_cor, y_cor, z_cor);
    }

    std::string getName() {
        return name;
    }

    void setCordinates(int aX, int aY, int aZ) {
        x_cor = aX;
        y_cor = aY;
        z_cor = aZ;
        std::cout << "Coordinates updated successfully" << std::endl;
    }

    
};

int main() {
    Drone drone("drone1", 239, 33, 32);
    std::cout << "Drone Name: " << drone.getName() << std::endl;

    // Print coordinates
    auto [x, y, z] = drone.getCordinates();
    std::cout << "Coordinates: (" << x << ", " << y << ", " << z << ")" << std::endl;

    return 0;
}
