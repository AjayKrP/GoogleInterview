from abc import ABC, abstractmethod


class PizzaStore(ABC):
    # common public method for all subclass, because main pizza store wants to control the how their order pizza works
    def order_pizza(self, type_):
        pizza = self.create_pizza(type_)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

    # Based on locality pizza tastes demands changes, so the method of creating pizza. Since its changing all over
    # the application that's why creating abstract method
    @abstractmethod
    def create_pizza(self, type_):
        pass


class PuneStylePizza(PizzaStore):

    def create_pizza(self, type_):
        if type_ == 'tomato':
            return _PuneStyleTomatoPizza()
        if type_ == 'onion':
            return _PuneStyleOnionPizza()
        if type_ == 'cheese':
            return _PuneStyleCheesePizza()

        raise ValueError('No such pizza found!')


class MumbaiStylePizza(PizzaStore):
    def create_pizza(self, type_):
        if type_ == 'tomato':
            return _MumbaiStyleTomatoPizza()
        if type_ == 'onion':
            return _MumbaiStyleOnionPizza()
        if type_ == 'cheese':
            return _MumbaiStyleCheesePizza()

        raise ValueError('No such pizza found!')


class Pizza(ABC):
    def __init__(self):
        self.__name = None

    def set_pizza_name(self, name):
        self.__name = name

    def get_pizza_name(self):
        return self.__name

    def prepare(self):
        print('preparing your pizza. Please wait for 10 mins ' + self.__name)

    def bake(self):
        print('baking your pizza ' + self.__name)

    def cut(self):
        print('cutting your pizza ' + self.__name)

    def box(self):
        print('boxing your pizza. your pizza is now ready for delivery ' + self.__name)


class _PuneStyleTomatoPizza(Pizza):
    def __init__(self):
        super(_PuneStyleTomatoPizza, self).__init__()
        self.set_pizza_name('Pune Style Tomato with garlic')


class _PuneStyleOnionPizza(Pizza):
    def __init__(self):
        super(_PuneStyleOnionPizza, self).__init__()
        self.set_pizza_name('Pune Style Onion with garlic')


class _PuneStyleCheesePizza(Pizza):
    def __init__(self):
        super(_PuneStyleCheesePizza, self).__init__()
        self.set_pizza_name('Pune Style Extra Cheese Pizza')


class _MumbaiStyleTomatoPizza(Pizza):
    def __init__(self):
        super(_MumbaiStyleTomatoPizza, self).__init__()
        self.set_pizza_name('Mumbai Style Tomato with garlic')


class _MumbaiStyleOnionPizza(Pizza):
    def __init__(self):
        super(_MumbaiStyleOnionPizza, self).__init__()
        self.set_pizza_name('Mumbai Style Onion with garlic')


class _MumbaiStyleCheesePizza(Pizza):
    def __init__(self):
        super(_MumbaiStyleCheesePizza, self).__init__()
        self.set_pizza_name('Mumbai Style Extra Cheese Pizza')

    def cut(self):
        print('cutting your mumbai style cheese pizza in rounded shape. ' + self.get_pizza_name())


if __name__ == "__main__":
    punePizza = PuneStylePizza()
    punePizza.order_pizza('tomato')
    print('========================================')
    mumbaiPizza = MumbaiStylePizza()
    mumbaiPizza.order_pizza('cheese')

from math import *


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'


class PolarFactory:
    @staticmethod
    def new_polar_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_cartesian_point(x, y):
        return Point(y * sin(x), x * cos(y))
