from math import sqrt, dist


def calc_distance(tup1, tup2):
    x1, y1, z1 = tup1
    x2, y2, z2 = tup2

    distance = sqrt(((x2-x1)**2)+((y2-y1)**2)+((z2-z1)**2))

    return distance

point1 = (2, 4, 6)
point2 = (4, 3, 7)

if __name__ == "__main__":
    print(calc_distance(point1, point2))
    print(dist(point1, point2))
    