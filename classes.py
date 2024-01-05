class Animal:
    '''Class Animal'''
    def __init__(self, name, size):
        self.name = name
        self.size = size

class Dog(Animal):
    '''Class Dog inherit from Animal'''
    def __init__(self, name, size, is_trained):
        super().__init__(name, size)
        self.is_trained = is_trained

class Cat(Animal):
    '''Class Cat inherit from Animal'''
    def __init__(self, name, size, is_hunter):
        super().__init__(name, size)
        self.is_hunter = is_hunter


dog1 = Dog('Spock', 'Medium', False)
cat1 = Cat('Luna', 'Small', True)

print(dog1.name, ('is a trained' if dog1.is_trained else 'is not trained'))
print(cat1.name, ('is a hunter' if cat1.is_hunter else 'is not a hunter'))
