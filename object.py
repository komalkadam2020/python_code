class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")


person = Person("Alice", 30)
person.say_hello()  # Output: Hello, my name is Alice and I'm 30 years old.
