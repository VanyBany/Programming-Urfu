class Circle:
    def __init__(self,radius):
        self._radius = radius  #защищенный атрибут


    @property
    def radius(self):
        # Доступ как к атрибуту: circle.radius
        return self._radius
    

    @radius.setter
    def radius(self,value):
        # Вызывается пр и circle.radius = значение

        if value <= 0:
            raise ValueError("Радиус должен быть положительным")
        self._radius = value


    @property
    def area(self):
        # Вычисляемое св-во - вызывается как атрибут
        return 3.14159 * self._radius ** 2
    
# Использование

circle = Circle(5)
print("Исходный радиус: {circle.radius}")

circle.radius = 10
print(circle.radius)
print("Новый радиус: {circle.radius}")
