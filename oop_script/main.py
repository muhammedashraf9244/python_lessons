"""
Main concepts of oop
    * Encapsulation
    * Data Hiding
    * Inheritance
    * Polymorphism

to create class
1- determine data member where is an instance(state of the object) or class variable
2- determine where the function

Class contain :
    1- instance variable vs class variable
        instance variable is a state of instance of object of class
        class variable is a shared instance variable betweeen instance Objects
             
        
    2- class mehtod vs instance variable vs static method
        instance method invokes your logic to change the state of the instance variable
        the class method invokes your logic to change behaviour over class 
        static method is a method related to the business of class

"""

from scripts.script_oop import Employee, Account


def main():
    emp1 = Employee(name="Ahmed", salary=7500,
                    address={'city': 'Beni Seuf', 'street': 'AAAA'},
                    department="HR")
    emp2 = Employee(name="Ashraf", salary=58.25,
                    address={'city': 'Beni Seuf', 'street': 'AAAA'},
                    department="Dev")
    # print('Emp1 ',emp1)
    # print('Emp2 ',emp2)
    # print('Emp2 counter ',emp2.counter)
    # print('Emp1 counter ',emp1.counter)
    
    # but when changing value of shared variable based on an instance object 
    # when access shared(static) variable from instance 
    # object convert this shared to instance variable belong to his instance object 
    
    # print('Emp1 active ',emp1.active)
    # print('Employee active ',Employee.active)
    # change shared data betweeen class 
    # Employee.active = False
    # print('Emp1 active ',emp1.active) 
    # print('Emp2 active ', emp2.active)
    # emp1.active = True
    # print('Emp1 Active ', emp1.active)
    # print(emp2.active)
    # print(Employee.active)
    # emp1.salary = -5
    # instance mehtod
    # print("Taxes ", emp1.get_taxes())
    # print("Counter Emp1 ", emp1.counter)
    # print("Counter Emp2 ", emp2.counter)
    # print("Counter Employee ", Employee.counter)
    # print('IncrementCounter on all instance')
    # Employee.increment_counter()
    # print("Counter Emp1 ", emp1.counter)
    # print("Counter Emp2 ", emp2.counter)
    # change counter shared to instance variable to object emp1
    # print("Change counter based on instance object")
    # emp1.increment_counter()
    # print("Counter Emp1 ", emp1.counter)
    # print("Counter Emp2 ", emp2.counter)
    # print("Chnage counter through instance method")
    # emp1.increment_counter_instance()
    # print("Counter Emp1 ", emp1.counter)
    # print("Counter Emp2 ", emp2.counter)
    # emp1_taxs = emp1.get_taxes()
    # print("Emp1 Taxes ", emp1_taxs)
    # print("Egypt Taxes ", emp1.convert_taxes(emp1_taxs))
    # print("Taxes on doller ", emp1.convert_taxes(emp1_taxs, 'USD'))
    
    # print(emp2.__dir__())
    # emp1.increment_counter_instance()
    # Employee.increment_counter()
    # Employee.increment_counter()
    # print("Counter Emp1 ", emp1.counter)
    # print("Counter Emp2 ", emp2.counter)
    # print("Counter Employee ", Employee.counter)
    # # print(f" Counter Objects {Employee.counter}")

    # print('Employee1 salary ', emp1.salary)
    # emp1.salary = 100
    # print('Employee1 salary ', emp1.salary)

    # accoun_ob = Account('Yousef', 4500, {'street': '5 street Shobra'}, 'BP', True)
    # print('Account 1')
    # print(accoun_ob)

    # print(f'Taxes for account {accoun_ob.get_taxes()}')

    accoun_ob = Account('Yousef', 4500, {'street': '5 street Shobra'}, 'BP', True)
    print('Account 1')
    print(accoun_ob)

    print(f'Taxes for account {accoun_ob.get_taxes()}')

    print("Property safe")
    print("Safe accoun_ob ", accoun_ob.safe)
    print("Safe accoun_ob ", accoun_ob._safe)
    # accoun_ob.safe = 'str' # raise ValueError
    accoun_ob.safe = True
    print("Safe accoun_ob ", accoun_ob.safe)
    print("Safe accoun_ob ", accoun_ob._safe)


if __name__ == "__main__":
    main()
