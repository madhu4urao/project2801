from abc import ABC, abstractmethod
class X(ABC):
    @abstractmethod
    def hi(self):
        pass
    @abstractmethod
    def hello(self):
        pass
class Y(X):
    def hi(self):
        print("hello X this is Y")
class Z(Y):
    def hello(self):
        print("hello Y this is Z")
z =Z()
z.hi()
z.hello()