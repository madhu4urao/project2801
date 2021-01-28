from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def display(self):
        pass
class B(A):
    def display(self):
        print("hello this is my first abstaction problem")
obj = B()
obj.display()
