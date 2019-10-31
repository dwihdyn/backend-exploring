# improvement:
# delete feature : ensure ID entereed exist

# initialisation
import getpass as gp


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Patient(Person):
    all = []
    count = 0

    def __init__(self, name, age, diagnose, patient_id):
        Person.__init__(self, name, age)
        Patient.count += 1
        self.diagnose = diagnose
        self.patient_id = Patient.count
        Patient.all.append(self)  # store all current data inside 'all'[] list

    def __repr__(self):
        return (f"ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, Diagnose: {self.diagnose}")


class Employee(Person):
    all = []
    count = 0

    def __init__(self, name, age, position, access_lvl, employee_id):
        Person.__init__(self, name, age)
        Employee.count += 1
        self.position = position
        self.access_lvl = access_lvl
        self.employee_id = Employee.count
        Employee.all.append(self)

    def __repr__(self):
        return (f"ID: {self.employee_id}, Name: {self.name}, Age: {self.age}, Position: {self.position}, Access Level: {self.access_lvl}")


# comment below 5 lines to start the database with clean slate
patient_1 = Patient("babi", 67, "heart attack", 1)
patient_2 = Patient("kid", 7, "kidney damage", 2)
patient_3 = Patient("another_kid", 8, "eye damage", 3)
emp_1 = Employee("Big Doctor", 40, 'Owner', 5, 1)
emp_2 = Employee("small potato", 17, 'cleaner', 1, 2)


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
            print("     2. Show selected record")
            print("     3. add record")
            print("     4. remove record")
            print(" ")
            print("=== EMPLOYEES ===")
            print("     5. Show all records")
            print("     6. Show selected record")
            print("     7. add record")
            print("     8. remove record")
            print(" ")
            print("     9. Exit")
            print("select your choice...")
            choice = int(input())
            if choice == 1:
                print("\n")
                print('-------------------------------------------')
                print("List of all patients : ")
                print("")
                # using loop so it print out neatly
                for _ in Patient.all:
                    print(_)
                print('-------------------------------------------')
                print("\n")

            elif choice == 2:

                print("\n")
                print('-------------------------------------------')
                for _ in Patient.all:
                    print(_)
                print(" ")
                print("enter the selected patient ID that you want to see : ")
                selected_patient = int(input())
                print("Checking database")
                j = 0
                while j <= 5:
                    print(".")
                    j += 1

                print("found a match!")
                for pat in Patient.all:
                    if pat.patient_id == selected_patient:
                        print(pat)
                print('-------------------------------------------')
                print("\n")

            elif choice == 3:
                print("\n")
                print('-------------------------------------------')
                new_pat_name = str(input("Enter new patient name : ....."))
                new_pat_age = int(input("Enter new patient age : ....."))
                new_pat_diagnose = str(
                    input("Enter new patient diagnosis : ....."))
                # since trigerring Patient() class will include appending new data action, just call Patient() to append data, no need .append again
                new_patient = Patient(
                    new_pat_name, new_pat_age, new_pat_diagnose, Patient.count)
                print('adding data to database')
                print(".")
                print(".")
                print('new patient successfully added to the database')
                print('-------------------------------------------')
                print("\n")

            elif choice == 4:
                print("\n")
                print('-------------------------------------------')
                for _ in Patient.all:
                    print(_)
                print(" ")
                remove_pnt_id = int(
                    input("Enter the patient ID that you wish to remove : "))

                pat_del_confirmation = str(
                    input("are you sure ? press y to confirm, any key to abort     "))
                if pat_del_confirmation == "y":
                    for i in Patient.all:
                        if i.patient_id == remove_pnt_id:
                            Patient.all.remove(i)
                    print('patient deleted successfully')
                else:
                    print('guess the patient has neither recovered......or dead')
                print('-------------------------------------------')
                print("\n")

            elif choice == 5:
                print("\n")
                print('-------------------------------------------')
                print("List of all employee")
                print(" ")
                # for loop to print out nicely row by row
                for _ in Employee.all:
                    print(_)
                print('-------------------------------------------')
                print("\n")

            elif choice == 6:
                print("\n")
                print('-------------------------------------------')
                for _ in Employee.all:
                    print(_)
                print(" ")
                print("enter the selected Employee ID that you want to see : ")
                selected_emp = int(input())
                print("Checking database")
                j = 0
                while j <= 5:
                    print(".")
                    j += 1
                print("found a match!")
                for emp in Employee.all:
                    if emp.employee_id == selected_emp:
                        print(emp)
                print('-------------------------------------------')
                print("\n")

            elif choice == 7:
                print("\n")
                print('-------------------------------------------')
                new_emp_name = str(input("Enter new employee name : ....."))
                new_emp_age = int(input("Enter new employee age : ....."))
                new_emp_pos = str(input("Enter new employee position : ....."))
                new_emp_acc_lvl = int(
                    input("Enter employee access level (lowest to highest, 1-5) : ....."))
                # since trigerring Employee() class will include appending new data action, just call Employee() to append data, no need .append again
                new_emp = Employee(
                    new_emp_name, new_emp_age, new_emp_pos, new_emp_acc_lvl, Employee.count)
                print('adding new employee to database')
                print(".")
                print(".")
                print('new employee successfully added to the database')
                print('-------------------------------------------')
                print("\n")

            elif choice == 8:
                print("\n")
                print('-------------------------------------------')
                for _ in Employee.all:
                    print(_)
                print(" ")
                remove_emp_id = int(input(
                    "Enter the employee ID that you wish to remove : "))
                emp_del_confirmation = str(
                    input("are you sure ? press y to confirm, any key to abort     "))
                if emp_del_confirmation == "y":
                    for i in Employee.all:
                        if i.employee_id == remove_emp_id:
                            Employee.all.remove(i)
                    print('employee successfully fired')
                else:
                    print('guess the employee didnt f****d up that bad.....yet')
                print('-------------------------------------------')
                print("\n")

            elif choice == 9:
                print("\n")
                print('-------------------------------------------')
                print(f"Logged out. Have a nice day {login_username}!")
                print('-------------------------------------------')
                print("\n")
                break

    elif login_username == "" and password_username == "":
        print("turning off........")
        break
    else:
        print("\n")
        print("wrong unsername/password! try again")
        print("\n")
