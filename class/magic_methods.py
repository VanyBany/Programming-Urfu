class Vector:

    def __init__(self,x,y):
        self.x = x
        self.y = y
    

    def __add__(self,other):
        # Сложение векторов: v1 + v2
        return Vector(self.x + other.x, self.y + other.y)
    

    def __mul__(self,  scalar):
        # Умножение на число: v * 5
        return Vector(self.x * scalar, self.y * scalar)
    

    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
v1 = Vector(2,3)
v2 = Vector(1,1)

print(v1 + v2)
print(v1 * 3)
