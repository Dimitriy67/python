# Реализуйте класс Vector, описывающий вектор на плоскости
# Также экземпляр класса Vector должен поддерживать приведение к типам bool, int, float и complex:
# при приведении к типу bool значением вектора должно являться значение True,
# если хотя бы одна его координата не равна нулю, или False в противном случае
# при приведении к типу int значением вектора должен являться его модуль в виде целого числа с отброшенной дробной частью
# при приведении к типу float значением вектора должен являться его модуль в виде вещественного числа
# при приведении к типу complex значением вектора должно являться комплексное число,
# вещественная часть которого равна координате вектора по оси x, мнимая часть — координате вектора по оси y

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def __float__(self):
        return (self.x**2 + self.y**2)**0.5

    def __int__(self):
        return int(float(self))

    def __complex__(self):
        return complex(self.x, self.y)


print(bool(Vector(1, 2)))
print(bool(Vector(1, 0)))
print(bool(Vector(0, 1)))
print(bool(Vector(0, 0)))