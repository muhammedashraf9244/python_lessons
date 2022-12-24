class Employee:
    # class variable 
    active = True
    salary = 2000

    def __init__(self, name:str, address, salary, department="Department1"):
        print("Starting creating the employee...")
        self.name = name
        self.address = address
        self.salary = salary
        self.department = department
        self.age = 0
        print("Finished creating the employee")

    @property
    def taxes(self):
        return self.salary * 0.20

    # def get_taxes(self):
    #     return self.salary * 0.20

    @classmethod
    def create_employee_from_string(cls, emp_data):
        split_data = emp_data.split(":")
        return cls(split_data[0], {"street": split_data[3]},
                   split_data[1], split_data[2])

    @staticmethod
    def convert_tax_to_egp(tax):
        return tax * 15.80

    def __str__(self):
        print(f'Employee info, name {self.name}, address {self.address} ')

class Accountant(Employee):
    def __init__(self, name, address, salary,
                 safe, department="Department1"):
        super().__init__(name, address, salary, department)
        self.safe = safe

    def get_safe_name(self):
        return self.safe

    def get_taxes(self):
        original_tax = super().get_taxes()
        return original_tax + 10


    def __str__(self):
        return f"{self.name} <{self.department}>"

emp1 = Employee(name=1, address={"street": "test"}, salary=5000)
acc1 = Accountant(name="Ahmed", address={}, salary=2000, safe="Safe1")

print(acc1)


# print(acc1.get_safe_name())
# print(acc1.taxes)
# acc1.salary = 1000
# print(acc1.taxes)

# emp2.calc_egp_salary()

# data = "Ali:5000:Department1:street1"
# emp3 = Employee.create_employee_from_string(data)


def check_division_by_three(num):
    if num % 3 == 0:
        return True
    return False



# my_filtered_numbers = []
# for i in my_numbers:
#     if check_div(i):
#         my_filtered_numbers.append(i)
#


# filter(lambda num: num % 3 == 0, my_numbers)
#
#
# output = map(lambda num: num ** 2, my_numbers)
# my_output = []
# for i in my_numbers:
#     my_output.append(i**2)




my_numbers = [1, 3, 5, 6, 8, 9]
my_output = []
for i in my_numbers:
    if i % 2 == 0:
        my_output.append(i**2)

my_output = [i ** 2 for i in my_numbers if i % 2 == 0]
my_dict_output = {i: i ** 2 for i in my_numbers if i % 2 == 0}
print(my_output)
print(my_dict_output)

