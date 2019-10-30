# initialisation
import getpass as gp


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Patients(Person):
    all = []

    def __init__(self, name, age, diagnose):
        Person.__init__(self, name, age)
        self.diagnose = diagnose
        Patients.all.append(self)  # store all current data inside 'all'[] list

    def __repr__(self):
        return f"({self.name}, {self.age}, {self.diagnose})\n"


class Employee(Person):
    all = []

    def __init__(self, name, age, position, access_lvl):
        Person.__init__(self, name, age)
        self.position = position
        self.access_lvl = access_lvl
        Employee.all.append(self)

    def __repr__(self):
        return f"({self.name}, {self.age}, {self.position}, {self.access_lvl})\n"


patient_1 = Patients("babi", 67, "heart attack")
patient_2 = Patients("kid", 7, "kidney damage")
patient_3 = Patients("another_kid", 8, "eye damage")
emp_1 = Employee("Big Doctor", 40, 'Owner', 5)
emp_2 = Employee("small potato", 17, 'cleaner', 1)


# start program

while True:
    print("Welcome to the hospital")
    print("-------------------------------------")
    print("enter username :")
    login_username = input()
    print("enter password :")
    password_username = gp.getpass()

    if login_username == 'admin' and password_username == str(111111):
        print(
            f"Welcome back {login_username}! what would you like to do today ?")
        while True:
            print("=== PATIENTS ===")
            print("     1. Show all records")
            print("     2. add record")
            print("     3. remove record")
            print(" ")
            print("=== EMPLOYEES ===")
            print("     4. Show all records")
            print("     5. add record")
            print("     6. remove record")
            print(" ")
            print("     7. Exit")
            print("select your choice...")
            choice = int(input())
            if choice == 1:
                print("\n")
                print('-------------------------------------------')
                print("List of all patients")
                print(Patients.all)
                print('-------------------------------------------')
                print("\n")

            elif choice == 2:
                print("\n")
                print('-------------------------------------------')
                print("Enter new patient data")
                print("sample format: (name, age, diagnosis)")
                new_patient = input()
                Patients.all.append(new_patient)
                print('new patient entered successfully')
                print('-------------------------------------------')
                print("\n")

            elif choice == 3:
                print("\n")
                print('-------------------------------------------')
                print("Select which patient do you want to remove: (enter index number)")
                print(Patients.all)
                del_patient = int(input())
                Patients.all.remove(Patients.all[del_patient])
                print('patient entered successfully')
                print('-------------------------------------------')
                print("\n")

            elif choice == 4:
                print("\n")
                print('-------------------------------------------')
                print("List of all employee")
                print(Employee.all)
                print('-------------------------------------------')
                print("\n")

            elif choice == 5:
                print("\n")
                print('-------------------------------------------')
                print("Enter new employee data")
                print("sample format: (name, age, position, access level (1-5))")
                new_employee = input()
                Employee.all.append(new_employee)
                print('new employee data entered successfully')
                print('-------------------------------------------')
                print("\n")

            elif choice == 6:
                print("\n")
                print('-------------------------------------------')
                print(
                    "Select which employee do you want to remove: (enter index number)")
                print(Employee.all)
                del_emp = int(input())
                Employee.all.remove(Employee.all[del_emp])
                print('patient entered successfully')
                print('-------------------------------------------')
                print("\n")

            elif choice == 7:
                print("\n")
                print('-------------------------------------------')
                print(f"Logged out. Have a nice day {login_username}!")
                print('-------------------------------------------')
                print("\n")
                break

    else:
        print("\n")
        print("wrong unsername/password! try again")
        print("\n")
