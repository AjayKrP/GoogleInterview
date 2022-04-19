class Singleton(object):
    _instance = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance[cls]


class Student(Singleton):
    pass


s1 = Student()
s1.name = 'ajay'
print(s1.name)
s2 = Student()
print(s2.name)
