"""
1. json will have key/value
2. it will support multiple dimentional array as value
"""
import re


class Element:
    def __init__(self, key, value):
        self.__key = key
        self.__value = value

    def get_key(self):
        return self.__key

    def get_value(self):
        return self.__value


a = {"name": [{"ajay": 1}]}
x = '{ "name":"John", "age":30, "city":"New York"}'


class Parser:
    def __init__(self):
        self.__data = []

    def parse_input(self, x):
        x = re.sub("[{}]", "", x)
        key_values = x.strip().split(',')
        return [key_value.strip() for key_value in key_values]


if __name__ == "__main__":
    parser = Parser()
    print(parser.parse_input(x))
