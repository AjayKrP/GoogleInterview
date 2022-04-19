class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    def area(self):
        return self._height * self._width


class Square(Rectangle):
    def __init__(self, size):
        super(Square, self).__init__(size, size)

    @Rectangle.width.setter
    def width(self, width):
        self._width = self._height = width

    @Rectangle.height.setter
    def height(self, height):
        self._width = self._height = height


def make_it(obj):
    w = obj.width
    obj.height = 20
    print(f'expected: {w * obj.height}, current result: {obj.area()}')


rc = Rectangle(4, 2)
make_it(rc)
sq = Square(3)
make_it(sq)

"""
If you're making child class with the help of interface then be careful,
Its not necessary that all child will behave same. For example---You're creating Bird Class 
with fly method in it and inheriting it to Ostrich & Parrot.
Here Ostrich cant fly bit it has method fly. which is not necessary 
"""
