## Single Inheritance
class Base:
    ### CHaracteristics -- proprties and actions
    pass

class Child(Base):
    ### Child class inherits the parents  class behiaviours/actions/methods etc.. & states/properties/variables/members etc..
    pass


## Multiple Inheritance
class A:
    pass

class B:
    pass

class C(A,B):
    pass


## Multi level Inheritance
class A:
    pass

class B(A):
    pass

class C(B):
    pass


## Hierachial Inheritance
class A:
    pass

class B(A):
    pass

class C(A):
    pass

## Hybrid Inheritance -- It is a combination of above all Inheritance.We can write in any form from above classes.It is like a Tree.
class Base:
   
    pass

class Child(Base):
    
    pass

class A:
    pass

class B(A):
    pass

class C(B):
    pass

class A:
    pass

class B(A):
    pass

class C(A):
    pass



## Multiple Inheritance Example
class A:
    def __init__(self) -> None:
        self.a = "A"
        print("in A")
class B:
    def __init__(self) -> None:
        self.a = "B"
        print("in B")


class Test(A,B): ## Left to Right
    def __init__(self) -> None:
        super().__init__()
        print("in Test")



##MRO: METHODS RESOLUTION ORDER

obj = Test()
print(obj.a)


#Here we are accessing protected members from another module(within the same package).
from inheritanceExample import Child

obj = Child()

"""
Object State: We can access these properties and methods here.
    properties:(c,d,_a,b) -- Here "b" is a instance variable which will be accessed only when we create "super().__init__()" inside child class.
    mehods:(show,describe)
"""

print(obj.show("another file")) #It returns "I am in another file class" and "None"


 