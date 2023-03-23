# Note:-Here class name should always start with Capital letter as a standard method.We can also write with small letters toobbut it is good practice to write capital letters.
class SavingsAccount:  #Here class name is "SavingsAccount".
    """
    Bank is a class with certain properties and actions

    Properties: ---- Member Variables / Member Properties -- States
        1. AccountHoldersName
        2. AccountNumber
        3. AccountType
        4. Balance
        5. AccountHoldersContactNumber

    Actions: ---- Member Methods / Member Functions -- Behaviours
        1. withdraw
        2. deposit
        3. check balance


    OOPS class have higher access control -- access specifiers
    """
    """
    Types of Acess specifiers: 1) public 2)private 3)protected
    """
    """
    Note: It is a good practice to write in camele case like "accountNumber" while we writing for variables as below:
    """
    """
    Note: If we create and access class variables/Members without creating constructor these class variables will become common to each and every "objects".Here object is 
    suppose each object is a person each person doesn't have common properties so inorder to avoid this conflict we must create constructor for every class.
    """
    """
    CLASS PROPERTIES -- It can be accessed to whole class for every object in class.These are common variables to every objects
    in class.These class properties are global properties.
    """
    __accountName = None        #Here double underscore defines the "variable" as a private.It cannot be shared different different objects(like methods) in same class.
    __accountNumber = None      #Here double underscore defines the "variable" as a private.It can be shared only within a class not outside the class.
    _accountPhoneNumber = None  #Here single underscore defines the "variable" as a protected.It can shared to different class like loan section or goldLoan section or creditCard section etc..But internally not outside.
    accountType = None          #Here there is no underscore.bcs here data is not confidential it is public.It can accesses to anywhere.
    __balance = None

    

    """
    Constructor will be called while creating the object.Here constructor is "def __init__()".
    """
    def __init__(self,accountName,phoneNumber,balance,type="savings") -> None: #Here "self" is an object.Suppose here self is a "saikiranAccount" it is an object.These are positional arguments.


        """
        Properties inside constructor are instance properties --- specific to object
        """

        self.__accountName = accountName        #It can also be written as "saikiranAccount.__accountName = accountName"
        self.__accountNumber = "123456789"      #It can also be written as "saikiranAccount.__accountNumber = "123456789""
        self._accountPhoneNumber = phoneNumber  #It can also be written as "saikiranAccount.__accountPhoneNumber = phoneNumber"
        self.accountType = type                 #It can also be written as "saikiranAccount.accountType = type"
        self.__balance = balance                #It can also be written as "saikiranAccount.__balance = balance"

    """
    Note: It is a good practice to write in snake_case like "check_balance" etc.. while we writing for functions as below:
    """
    
    def show_details(self):
        print("Details of Account Holder:")
        print(f"Name:{self.__accountName}")
        print(f"Phone Number:{self._accountPhoneNumber}")
        print(f"Account Type:{self.accountType}")

    def set_accountName(self,name): #Here we need to write compulsary "set_variablename" we must write "set" as a covention. 
        self.__accountName = name

    def get_accountName(self):      #Here we need to write compulsary "get_variablename" we must write "get" as a covention. 
        return self.__accountName

    def widthdraw(self):
        pass
    def deposit(self):
        pass
    def check_balance(self):
        pass


#Here "saikiranAccount" is  one object.
saikiranAccount = SavingsAccount("Saikiran",7671083785,2500)  ## Object Initializing State -- First Object State
saikiranAccount.show_details()
#Here public class variables are accessed and updated outiside the class except private variables
saikiranAccount.accountType = "ahghjsjsa"
saikiranAccount.show_details()

#Here account name is "private variable/Member" and also it is "class variable/Global variable" it can only be changed/updated using Setter & Getter methods.
#saikiranAccount.__accountName = " SAI KUMAR"
#saikiranAccount.show_details()

#We can update private variables and accessed using "Setter & Getter" methods
saikiranAccount.set_accountName("SAI KUMAR")
saikiranAccount.show_details()

obj = SavingsAccount("random",88654,"savings",2500)
obj.show_details()