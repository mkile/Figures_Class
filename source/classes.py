from functools import reduce
from math import pi, inf


class Figure:
    def __init__(self, name: str, sides_list: list, sides: int):
        if 0 in sides_list:
            raise Exception('Создание фигур с параметром равным 0 запрещено.')
        if self.__class__.__name__ == 'Figure':
            raise Exception('Создание объектов класса Figure запрещено.')
        if len(name) == 0:
            raise Exception('Имя фигуры не может быть пустым!')
        self.name = name
        if len(sides_list) != sides:
            raise Exception('Количество сторон фигуры не соответствует фигуре,' +
                            'передано: ' + str(len(sides_list)) + ' ,а должно быть: ' + str(sides))
        self.sides_list = sides_list
        self.__sides = sides
        if sides == 1:
            self.angles = inf
        else:
            self.angles = sides

    def __repr__(self):
        return '<' + Figure.__name__ + '>' + \
               self.name + ':' + str(self.__sides)

    def area(self):
        sides_set = list(set(self.sides_list))
        if len(sides_set) == 1:
            return sides_set[0] ** 2
        else:
            return sides_set[0] * sides_set[1]

    def perimeter(self):
        return sum(self.sides_list)

    def add_area(self, other):
        if not isinstance(other, Figure):
            raise Exception('Метод принимает только объекты '
                            'наследуемые от класса Figure.')
        return self.area() + other.area()


class Rectangle(Figure):
    sides = 4

    def __init__(self, name, sides_list):
        super().__init__(name, sides_list * 2, self.sides)


class Square(Figure):
    sides = 4

    def __init__(self, name, sides_list):
        super().__init__(name, sides_list * 4, self.sides)


class Triangle(Figure):
    sides = 3

    def __init__(self, name, sides_list):
        super().__init__(name, sides_list, self.sides)
        if not self.__check_possibility():
            raise Exception('Треугольника с такими сторонами существовать не может')

    def __check_possibility(self):
        sides = self.sides_list + self.sides_list
        for side_number in range(0, len(sides) - 3):
            if sides[side_number] > (sides[side_number + 1] + sides[side_number + 2]):
                return False
        return True

    def area(self):
        return (self.perimeter() / 2 *
                reduce(lambda x, y: x * y,
                       [self.perimeter() / 2 - x for x in self.sides_list])) ** 0.5


class Circle(Figure):
    sides = 1

    def __init__(self, name, sides_list):
        super().__init__(name, sides_list, self.sides)

    def area(self):
        return pi * self.sides_list[0] ** 2

    def perimeter(self):
        return 2 * pi * self.sides_list[0]


if __name__ == '__main__':
    print('Hello')
