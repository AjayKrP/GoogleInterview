# from abc import ABC, abstractmethod
# from time import time_ns
#
#
# class Entry(ABC):
#     name: str
#     created_at: int
#     update_at: int
#     last_accessed: int
#
#     def __init__(self, name, directory):
#         self.name = name
#         self.parent = directory
#         self.created_at = time_ns()
#         self.update_at = time_ns()
#         self.last_accessed = time_ns()
#
#     def getFullPath(self):
#         if self.parent is None:
#             return self.name
#         return self.parent.getFullPath + '/' + self.name
#
#     def getCreationTime(self):
#         return self.created_at
#
#     def getUpdationTime(self):
#         return self.update_at
#
#     def getLastAccessedTime(self):
#         return self.last_accessed
#
#     @abstractmethod
#     def getSize(self):
#         pass
#
#
# class File(Entry):
#     __content: str
#     size: int
#
#     def __init__(self, name, directory, size):
#         super().__init__(name, directory)
#         self.size = size
#
#     def getSize(self):
#         return self.size
#
#     def getContent(self):
#         return self.__content
#
#     def setContent(self, __content):
#         self.__content = __content
#
#
# class Directory(Entry):
#     __contents: []
#
#     def __init__(self, name, directory):
#         super().__init__(name, directory)
#         self.__contents = []
#
#     def getSize(self):
#         size = 0
#         for entry in self.__contents:
#             size += entry.getSize()
#         return size
#
#     def deleteEntry(self, entry):
#         self.__contents.remove(entry)
#
#     def addEntry(self, entry):
#         self.__contents.append(entry)
#
#     def getContents(self):
#         return self.__contents
#
#     def numberOfFiles(self):
#         count = 0
#         for entry in self.__contents:
#             if isinstance(entry, Directory):
#                 count += 1
#                 count += entry.numberOfFiles()
#             elif isinstance(entry, File):
#                 count += 1
#         return count
#
#
# if __name__ == "__main__":
#     d1 = Directory('folder1', None)
#     file1 = File('file1', d1, 20)
#     d1.addEntry(file1)
#
#     d2 = Directory('folder2', d1)
#     d1.addEntry(d2)
#
#     print(d1.numberOfFiles())

from abc import abstractmethod, ABC
from datetime import datetime


class Entry(ABC):
    def __init__(self, name, directory):
        self.name = name
        self.parent = directory
        self.created_at = datetime.now()
        self.update_at = datetime.now()
        self.last_accessed_at = datetime.now()

    @abstractmethod
    def getSize(self):
        pass

    def getLastAccessTime(self):
        return self.last_accessed_at

    def getCreationTime(self):
        return self.created_at

    def getUpdatedAt(self):
        return self.update_at


class File(Entry):
    def __init__(self, name, directory, size):
        super(File, self).__init__(name, directory)
        self.size = size
        self.__content = None

    def getSize(self):
        return self.size

    def getFullPath(self):
        if self.parent is None:
            return self.name
        return self.parent.getFullPath + '/' + self.name

    def setContent(self, __content):
        self.__content = __content

    def getContent(self):
        return self.__content


class Directory(Entry):
    def __init__(self, name, directory):
        super(Directory, self).__init__(name, directory)
        self.__contents = []

    def getSize(self):
        size = 0
        for entry in self.__contents:
            size += entry.getSize()
        return size

    def numberOfFiles(self):
        count = 0
        for entry in self.__contents:
            if isinstance(entry, Directory):
                count += 1
                count += entry.numberOfFiles()
            elif isinstance(entry, File):
                count += 1
        return count

    def addContent(self, entry):
        self.__contents.append(entry)

    def removeContent(self, entry):
        self.__contents.remove(entry)
