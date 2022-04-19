from abc import abstractmethod


# interface segregation principle
class Machine:
    @abstractmethod
    def print(self, document):
        raise NotImplementedError

    @abstractmethod
    def scan(self, document):
        raise NotImplementedError

    @abstractmethod
    def fax(self, document):
        raise NotImplementedError


class NewFashionedPrinter(Machine):
    def print(self, document):
        pass

    def scan(self, document):
        pass

    def fax(self, document):
        pass


class OldFashionedPrinter(Machine):
    def print(self, document):
        pass

    """
    What happen if old fashion printer doesnt support scan, fax
    client have to unnecessarily implement code which is not required, So Idea is
    to break down large interface to smaller ones
    """

    def scan(self, document):
        pass

    def fax(self, document):
        pass


class Printer:
    @abstractmethod
    def print(self, document):
        pass


class Scanner:
    @abstractmethod
    def scan(self, document):
        pass


class MultiFunctionedMachine(Printer, Scanner):
    def scan(self, document):
        pass

    def print(self, document):
        pass


"""
Here we have broken down large interface into several smaller interface  

1. no code should be forced to depend on methods it does not use
2.  ISP splits interfaces that are very large into smaller and more specific
 ones so that clients will only have to know about the methods that are of interest to them.
3. Such shrunken interfaces are also called role interfaces
4. ISP is intended to keep a system decoupled and thus easier to refactor, change, and redeploy. I
5. 
"""
