class circle():
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius

c = circle(5)
print(c.diameter)

c.radius = 7
print(c.diameter)

print(c.radius)
