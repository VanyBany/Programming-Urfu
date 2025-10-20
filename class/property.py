class Circle:
    def __init__(self,radius):
        self._radius = radius  #защищенный атрибут


    @property
    def radius(self):
        # Доступ как к атрибуту: circle.radius
        return self._radius

    @property
    def area(self):
        # Вычисляемое св-во - вызывается как атрибут
        return 3.14159 * self._radius ** 2
    
# Использование

circle = Circle(5)

print(circle.radius())
# print(circle.area())
# print(circle.area)