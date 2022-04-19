from enum import Enum
from abc import ABC, abstractmethod


class Relationship(Enum):
    PARENT = 1
    CHILD = 2


class Person:
    def __init__(self, name):
        self.name = name


class RelationshipGetter:
    @abstractmethod
    def get_children_of(self, name):
        pass


class RelationshipGraph(RelationshipGetter):  # Notice
    def __init__(self):
        self.relationships = []

    def create_relationship_graph(self, parent, child):
        self.relationships.append(
            (parent, Relationship.PARENT, child)
        )
        self.relationships.append(
            (child, Relationship.CHILD, parent)
        )

    def get_children_of(self, name):
        for p in self.relationships:
            if p[0].name == name and p[1] == Relationship.PARENT:
                yield p[2].name


class Search:
    # def __init__(self, relationship_graph): # Not need to pass relationship_graph
    #     self.relations_graph = relationship_graph

    """
    Here we have created dependency on the Low Level Classes(Tightly Coupled)
    Suppose in future if some data structure changes at low level classes then 
    this code will also have to change accordingly. So we want to avoid this kind
    of breakage. Solution: Create a separate interface to handle this kind of problem 
    """
    # def get_children_of(self, name):
    #     for p in self.relations_graph.relationships:
    #         if p[0].name == name and p[1] == Relationship.PARENT:
    #             yield p[2].name

    def __init__(self, getter):
        for p in getter.get_children_of('Jay Krishna Pandit'):
            print(p)


parent = Person('Jay Krishna Pandit')
child1 = Person('Ajay Pandit')
child2 = Person('Vijay Pandit')

rg_graph = RelationshipGraph()
rg_graph.create_relationship_graph(parent, child1)
rg_graph.create_relationship_graph(parent, child2)

s = Search(rg_graph)

"""
1. In object-oriented design, the dependency inversion principle is a specific
 methodology for loosely coupling software modules
2. High-level modules should not import anything from low-level modules. Both should 
depend on abstractions (e.g., interfaces).
3. Abstractions should not depend on details. Details (concrete implementations) should
 depend on abstractions.
"""