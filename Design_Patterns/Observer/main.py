from abc import ABC, abstractmethod


# class Observable:
#     def __init__(self):
#         self.methods = []
#
#     def attach(self, method):
#         if method not in self.methods:
#             self.methods.append(method)
#         else:
#             raise ValueError(f'{method.name} is already present!')
#
#     def detatch(self, method):
#         if method in self.methods:
#             self.methods.remove(method)
#         else:
#             raise ValueError(f'{method.name} not found!')
#
#     def notify(self):
#         for method in self.methods:
#             method.update()
#
# class Event(ABC):
#     @abstractmethod
#     def update(self):
#         pass
#
# class NewsEvent(Event):
#     def update(self):
#         print('printing from News event')


class Observable:
    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def notify(self, obs):
        for observer in self.observers:
            if observer != obs:
                observer.update()

    def unsubscribe(self, observer):
        self.observers.remove(observer)


class Observer(Observable):
    def __init__(self):
        super(Observer, self).__init__()
        self._state = None

    @abstractmethod
    def update(self, *args, **kwargs):
        pass

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, new_state):
        self._state = new_state
        self.notify(self)


class NewsEvent(Observer):
    def update(self, *args, **kwargs):
        print('from news event')


class DJEvent(Observer):
    def update(self, *args, **kwargs):
        print('from DJ event')


if __name__ == "__main__":
    nv = NewsEvent()
    dv = DJEvent()

    print(len(nv.observers))
    nv.state = 1
    dv.state = 2



        
            
