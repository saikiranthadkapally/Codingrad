class Human: ## Capital Camel Case
    # Class Property
    count = 0
    __abc = None
    def __init__(self,name,color="grey") -> None:
        ## Instance Properties
        self.__color = color
        self.name = name
    
    ### Instance Method -- This method will only be called by "object".We can't call by "class name".
    def eat(self):  #For instance method "self" parameter is important.
        print(f"{self.name} with color {self.__color}")

    @classmethod #For class method "cls" parameter is important.
    def increase(cls):
        cls.count = cls.count+1
    
    ## Getters
    def get_color(self):
        return self.__color
    
    ## Setters
    def set_color(self,color):
        self.__color = color

    @staticmethod #In static method it doesnot need any parameter.
    def abc():
        return "Static Method" #Instead of "return" if we write "print()" it will execute and print "None" in terminal.

def main():
    print("Example of OOPS")
    obj1 = Human("Saikiran","white") ### count = 0, color = white, name = Saikiran -- object state
    print(f"Object Details:{obj1.get_color()}")
    print(f"Name of the Object:{obj1.name}")
    print(f"Class Property Accessing from class:{Human.count}")
    print(f"Class Property accessed from obj {obj1.count}")
    obj1.increase() ### self, cls(class) both will be passed automatically
    print(f"Object count in a class is {Human.count}")
    obj2 = Human("Savinay")
    obj2.increase()
    print(f"Object count in a class is {Human.count}")
    Human.increase()
    print(f"Object count in a class is {Human.count}")
    # print(f"Accessing Instance method {Human.eat()}") -- only cls will be passed. so it throws error which is a "typeerror".Inorder to solve such type of errors we use decorators "@staticmethod"
    print(f"calling static method:{Human.abc()}")      
                                                 
'''
Every file is treated as a "main module" by default.So the "main" module name is accessed by CPU in the first step.Here "__main__" is 
a module.In below it can also aexecute without writing "main" module but it is a good practice to write for a proper way as we used to 
written in c,c++,java.So here we are writing the "main" module conventionally for a sequence of execution in a good way. 
'''    
if __name__ == "__main__":
    main()
   
        