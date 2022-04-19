from abc import ABC, abstractmethod


class Context:
    def __init__(self):
        self.type = None

    def setContext(self, type):
        self.type = type

    def execute(self, value):
        if self.type is None:
            raise ValueError('Type is not defined yet!')
        self.type.execute(value)


class Search(ABC):
    @abstractmethod
    def execute(self, value):
        pass


class SearchByName(Search):
    def execute(self, value):
        print(f'you are searching by some name: {value}')


class SearchBySKU(Search):
    def execute(self, value):
        print(f'you are searching by some SKU: {value}')


class SearchByNameAndSKU(Search):
    def execute(self, value):
        print(f'you are searching by Name & SKU: {value}')


if __name__ == "__main__":
    context = Context()

    context.setContext(SearchByName())
    context.execute('apple')

    context.setContext(SearchBySKU())
    context.execute('D00012')
