import copy


class Address:
    def __init__(self, street_address, city, country):
        self.street_address = street_address
        self.city = city
        self.country = country

    def __str__(self):
        return f'{self.street_address}, {self.city}, {self.country}'


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} lives at {self.address}.'


class EmployeeFactory:
    __proto = Person('', Address('Hinjewadi Phase 1', 'Pune', 'Maharastra'))

    @staticmethod
    def __new__object(proto, name):
        result = copy.deepcopy(proto)
        result.name = name
        return result

    def get_new_employee(self, name):
        return EmployeeFactory.__new__object(self.__proto, name)
    
"""
ajay = Person('', Address('Hinjewadi Phase 1', 'Pune', 'Maharastra'))
print(ajay)
# deepak = copy.copy(ajay) shallow copy wont work here
deepak = copy.deepcopy(ajay)
deepak.name = 'Deepak'
print('=====')
print(ajay)
print(deepak)
"""

ef = EmployeeFactory()
ajay = ef.get_new_employee('Ajay')
deepak = ef.get_new_employee('Deepak')

print(ajay)
print(deepak)
