import math


class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def cal_p(self):
        return 2 * math.pi * self.r

    def cal_a(self):
        return self.r ** 2 * math.pi


# main

c = Circle(4, 3, 7)
print("Perimeter:     ", round(c.cal_p(), 2))
print("Area:", round(c.cal_a(), 2))
