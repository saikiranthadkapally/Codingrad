class Base:
#Here we are able to access protected properties from its child class.But private propperties even though it is child class we can't access.
    _a = "Class Property -- Base" 
    def __init__(self) -> None:
        self.b = "Instance Proprty -- Base"

    def show(self,className): ## public member instance method
        print(f"I am in {className} class")

    def describe_obj(self,className):
        self.show(className)
        print(f"Object Class Property:{self._a}\nObject Instance Property:{self.b}")
'''
While it's true that the properties of the parent class are automatically inherited by the child class, calling super().__init__() in 
the child class __init__() method is necessary to ensure that the parent class's __init__() method is also called during object creation.
When you create an instance of the child class, the __init__() method of the child class is called first. If the child class does not 
call super().__init__(), the parent class's __init__() method will not be called, and any instance properties that the parent class 
initializes in its __init__() method will not be set.This means that if you try to access any instance properties of the parent class 
that were not explicitly set in the child class, you will get an AttributeError because those properties were not initialized.By calling
super().__init__() in the child class __init__() method, you ensure that the parent class's __init__() method is called and any necessary
instance properties are initialized. This allows you to access all inherited properties of the parent class without getting any 
AttributeError exceptions.

**Note**: If you do not define an __init__() method in the child class, the parent class's __init__() method will be automatically inherited
and called during object creation. In this case, you do not need to explicitly call super().__init__() in the child class, as it will be
called automatically.
'''

class Child(Base):
    c = "Class Proprty-- Child"
    def __init__(self) -> None: #"Constructor" of child class wont't call automatically Base class "constructor"
#"super()" is a keyword which will be able to make you access to the parent class properties and functions.
        super().__init__()  #Here Inorder to call "constructor" of base class we must use "super().__init__".otherwise it throws error.
        self.d = "Instance Property -- Child"
'''
Here these two are optional.In case we need to update or override then we need to write and make changes according to us.It means we
can also extend or add extra properties to it.
'''
    # def show(self, className): #In child class we can also override or update the base class functions and properties.
    #     return super().show(className) # "super()" will be replace with the base class.So here "super()" is replaced with "Base" class.
    
    # def describe_obj(self, className):
    #     return super().describe_obj(className) # "super()" will be replace with the base class.So here "super()" is replaced with "Base" class.

    # _a ="funshoot" # For protected properties we can also override or update from child class too.
    # print(_a)

def main():
    obj = Base()
    obj.describe_obj("Base")

    child_obj = Child()
    
    """
    Object State:
        properties:(c,d,_a,b) -- Here "b" is a instance variable which will be accessed only when we create "super().__init__()" inside child class.
        mehods:(show,describe)
    """
    
    """
    Here "child_obj" is an object of child class it indirectly access to parent class "instance variable" so in "Child" class we must
    write "super().__init__()" otherwise it throws "AttributeError"
    """
    child_obj.describe_obj("Child") #Using child object we are called parent class function by passing "Child" as a parameter.

    # _a = "ginshot"  # For protected properties in base class we can also override or update from outside the class too.
    # print(_a)
    # _c = "onion" # For protected properties in child class we can also override or update from outside the class too.
    # print(_c)
   
    print(child_obj.b) #Here this "b" is an "instance property" of parent class.so we must write "super().__init__()" in child class.

if __name__ == "__main__":
    main()


