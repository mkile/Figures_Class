class Figure:
    def __init__(self, name: str, sides_list: list, sides: int):
        self.name = name
        if len(sides_list) != sides:
            raise Exception('Количество сторон фигуры не соответствует фигуре.')
        self.sides_list = sides_list
        self.__sides = sides

    def __repr__(self):
        return '<' + Figure.__name__ + '>' + \
               self.name + ':' + str(self.__sides)

    def area(self):
        if len(set(self.sides_list)) == 1:
            return self.sides_list[0] ** 2
        else:
            return set(self.sides_list)[0] * set(self.sides_list)[1]

    def perimeter(self):
        return sum(self.sides_list)

    def add_figure(self, other):
        if not isinstance(other, Figure):
            raise Exception('Можно складывать только объекты класса Figure')
        return self.area() + other.area()


class Rectangle(Figure):
    sides = 4

    def __init__(self, name, sides_list):
        super().__init__(name, sides_list * 2, self.sides)


x = Rectangle('rect', [5, 5])
y = Rectangle('rect', [5, 5])
print(x.area())
print(x.perimeter())
print(x)
print(x.add_figure(5))
