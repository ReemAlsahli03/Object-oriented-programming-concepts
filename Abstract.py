import abc

class abstract(object):
    #ABCMeta will mark this classas abstract class
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def Dog(self, name):
        return

    @abc.abstractmethod
    def cat(self, name):
        return


#End of abstract class

class Animal(abstract):
    def Dog(self, name):
        self.name = name
        print(name)
    def cat(self):
        print("Abstract method")

    def Bird(self):
        print("instance method ")


Obj1 = Animal()
Obj1.Dog("mikey")
Obj1.cat()
Obj1.Bird()
