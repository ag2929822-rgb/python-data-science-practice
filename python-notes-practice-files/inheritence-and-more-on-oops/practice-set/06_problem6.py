class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, v2):
        return Vector(self.x + v2.x, self.y + v2.y, self.z + v2.z)

    def __mul__(self, v2):
        return self.x * v2.x + self.y * v2.y + self.z * v2.z

    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"


v1 = Vector(7, 8, 10)
v2 = Vector(1, 2, 3)

print(v1)        # 7i + 8j + 10k
print(v1 + v2)   # 8i + 10j + 13k
print(v1 * v2)   # dot product
