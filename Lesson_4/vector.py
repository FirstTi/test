

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distanse(self):
        return (self.x ** 2 + self.y ** 2) ** (1/2)

point = Point(5, 7)
print(point.distanse())



