class Employee(object):
    # class variable
    active: bool = True
    counter: int = 1

    def __init__(self, name: str, salary: float, address: dict, department: str) -> None:
        # instance variable
        self.name: str = name
        self._salary: float = salary
        self.address: dict = address
        self.department: str = department
        print('Successfully Create Object Employee')

    # instance method
    def get_taxes(self) -> float:
        return self._salary * .50

    # to calc taxes as property
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        print("In _salary")
        if salary <= 0:
            raise ValueError('No pass salary less than or equal 0')
        else:
            self._salary = salary

    # class method
    # cls implicit refernce to class not instance of object
    @classmethod
    def increment_counter(cls):
        cls.counter += 1

    def increment_counter_instance(self):
        self.counter += 1

    # class method for create object from string
    @classmethod
    def create_object(cls, string_object):
        string_split = string_object.split(":")
        return cls(string_split[0], float(string_split[1]), {'street': string_split[2]}, string_split[3])

    # static method
    @staticmethod
    def convert_taxes(taxes, currency='EGP'):
        if currency == 'EGP':
            return taxes
        elif currency == 'USD':
            return taxes * 20.8
        else:
            return taxes

    # magic function
    def __str__(self):
        return f"name -> {self.name} salary -> {self.salary} department -> " \
               f"{self.department} address -> {self.address}"


'''
Python support inheritance and super keyword to Overriding 
In Python no there are access modifiers but if we want to make access modifiers private using 
__property
__method

'''


class Account(Employee):
    def __init__(self, name, salary, address, department, safe=None):
        # this is repeate code not OOP
        # self.name=name
        # self.salary=salary
        # self.address=address
        # self.department=department        

        # Overriding __init__
        super().__init__(name, salary, address, department)
        self._safe:bool = safe

    @property
    def safe(self):
        print("In property")
        return self._safe
    
    @safe.setter
    def safe(self, safe):
        print("In Settter ", safe)
        if isinstance(safe, str):
            raise ValueError("You must be pass a bool value")
        if safe:
            self._safe = False
        else:
            self._safe = True
            
    
    def __str__(self):
        print_object = super().__str__()
        return print_object + f'\nsafe -> {self.safe}'

    
    def get_taxes(self):
        origin_taxes = super().get_taxes()
        return origin_taxes + 10


def main():
    # we can call the constructor with named parameters or positional parameters
    emp1 = Employee(name="Ahmed", salary=36.25, address={'street': '4 Taha'}, department="HR")
    Employee.increment_counter()
    emp2 = Employee("Muhammed", 50.6, {'street': '5 ADD'}, "Sales")
    Employee.increment_counter()
    print("Employee 1")
    print(emp1)
    print(f" Counter Objects {Employee.counter}")

    """
    not use this for declartion instance variable  
    emp1.email="ssed@dd.com"
    print(emp1.email)
    print(emp2.email)  # error
    """

    # Accesss class variable using instance of object 
    emp1.active = False
    print(emp1.active)
    print(emp2.active)

    # Accesss class variable using name of class this change can apply for all object not use this class variable
    Employee.active = True
    print(emp1.active)
    print(emp2.active)

    """
    Instance variable vs Class variable
    instance variable is only for instance of object if can access using class name not change state of
    instance of object
    Class or Static variable is shared with all object and can access using class name and change state of instance
    """
    emp3 = Employee("Mohamoud", 1000, {'street': '5 Biba'}, "Development")

    Employee.active = False
    print(emp1.active)
    print(emp2.active)
    print(emp3.active)

    # not use class name to access instance varaible 
    #  Employee.name = "Ashraf" 
    # print(emp1.name)
    # print(emp2.name)
    # print(emp3.name)

    taxes_emp1 = emp1.get_taxes()
    print(f"Taxes emp1 {taxes_emp1}")

    empl_object = Employee.create_object("Ashraf:205:5 Giza:Sales")
    print(empl_object.name, empl_object.address, empl_object.salary, empl_object.department)

    egypt_taxes = empl_object.convert_taxes(empl_object.get_taxes())
    print(f"egypt taxes {egypt_taxes}")

    print('Employee object ')
    print(empl_object)

    print('taxes property ')
    print(empl_object.mytax)

    accoun_ob = Account('Yousef', 4500, {'street': '5 street Shobra'}, 'BP', True)
    print('Account 1')
    print(accoun_ob)

    print(f'Taxes for account {accoun_ob.get_taxes()}')


if __name__ == "__main__":
    main()
