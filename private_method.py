class MyClass:
    def __init__(self):
        self.__private_method()

    def __private_method(self):
        print("This is a private method")


my_obj = MyClass()  # Output: This is a private method
#my_obj.__private_method()  # Raises an AttributeError
