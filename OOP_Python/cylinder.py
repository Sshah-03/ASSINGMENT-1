class cylinder:
    def __init__(self, height, radius):
        self.height = height
        self.radius = radius
    def volume(self):
        return self.height * 3.14 * (self.radius)**2
    def surface(self):
        top = 3.14 * (self.radius **2)
        return (2 * top) + (2 * 3.14 * self.radius * self.height)
mycyl = cylinder(2,3)
print(mycyl.volume())
print(mycyl.surface())

        