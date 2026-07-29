# Task 5: Extending a Class

# declare point class
class Point:
    # initialize method with self, x, y params
    def __init__(self, x, y):
        # initialize point x
        self.x = x
        # initialize point y
        self.y = y

    # equality method
    def __eq__(self, other):
        # return true if both x and y coordinates match, otherwise false
        return self.x == other.x and self.y == other.y

    # string representation method
    def __str__(self):
        # return str of coordinates
        return f"Point({self.x}, {self.y})"

    # distance method
    def distance(self, other):
        # return calculated distance
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

# declare vector subclass
class Vector(Point):
    # string representation method
    def __str__(self):
        # return str of vectors
        return f"Vector({self.x}, {self.y})"

    # addition method
    def __add__(self, other):
        # return new vector with added coordinates
        return Vector(self.x + other.x, self.y + other.y)

p1 = Point(0, 8)
p2 = Point(1, 9)
p3 = Point(0, 8)

print(p1) #Point(0, 8)

print(p1 == p3) #true
print(p1 == p2) #false

print(p1.distance(p2)) #((0 - 1) ** 2 + (8 - 9) ** 2) ** 0.5 = 1.4142135623730951

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2 #Vector(1 + 3), (2 + 4)

print(v3) #Vector(4, 6)
print(v3.distance(v1)) #((4 - 1) ** 2 + (6 - 2) ** 2) ** 0.5 = 5.0