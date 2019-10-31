class Hospital():
    def __init__(self, hospital_name, location, number_of_employees, number_of_patients):
        self.hospital_name = hospital_name
        self.location = location
        self.number_of_employees = number_of_employees
        self.number_of_patients = number_of_patients


hospital = Hospital("Moonway Medical", "Moonway", "3", "2")


class People():
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation


class Patient(People):
    all = []
    count = 0

    def __init__(self, name, occupation, condition, patient_id):
        People.__init__(self, name, occupation)
        Patient.count += 1
        self.condition = condition
        self.patient_id = Patient.count
        Patient.all.append(self)

    def __repr__(self):
        return(f"ID:{self.patient_id}  | Name: {self.name}  | Occupation: {self.occupation}  | Condition: {self.condition}")


class Employee(People):
    all = []
    count = 0

    def __init__(self, name, occupation, access_level, employee_id):
        People.__init__(self, name, occupation)
        Employee.count += 1
        self.access_level = access_level
        self.employee_id = Employee.count
        Employee.all.append(self)

    def __repr__(self):
        return(f"ID:  {self.employee_id}  | Name: {self.name}  | Occupation: {self.occupation}  | Access Level: {self.access_level}")


employee_1 = Employee("John", "Janitor", "Ground Staff", 1)
employee_2 = Employee("Adrian", "Doctor", "Medical Staff", 2)
employee_3 = Employee("Cass", "CEO", "SUPERADMIN", 3)
patient_1 = Patient("Shawn", "Student", "Sleepiness", 1)
patient_2 = Patient("Ismail", "Student", "Broken arm", 2)


# program start
print(f"Welcome to {hospital.hospital_name}")
print("==========================")
login = False
while login == False:
    print("Please enter your username:")
    username = input("username:  ")
    print("Please enter your password:")
    password = input("password:  ")
    if username == "admin" and password == "111111":
        print("Welcome Cass! Your access level is: SUPER ADMIN")
        login = True
        status = "SUPER ADMIN"
    elif username == "adrian" and password == "123456":
        print("Welcome Adrian! Your access level is: Medical Staff")
        login = True
        status = "DOCTOR"
    else:
        print("Wrong username or password!!")
        print("============================")

if status == "SUPER ADMIN":
    option = 0
    while option != "9":         # if option ="9" program is closed
        print("======================")
        print("What would you like to do?")
        print("Options:")
        print(" 1. list_patients")
        print(" 2. view_records <patient_id>")
        print(" 3. add_patient")
        print(" 4. remove_record <patient_id> <record_id>")
        print(" 5. list_employees")
        print(" 6. view_records <employee_id>")
        print(" 7. add_record <employee_id>")
        print(" 8. remove_record <employee_id> <record_id>")
        print(" 9. exit")
        option = input("Please choose an option: ")

        # option 1
        if option == "1":
            print("Patient List")
            print("=======================")
            for patient in Patient.all:
                print(patient)

        # option 2
        elif option == "2":
            patient_index = int(
                input("Enter patient ID to check records:     "))
            for patient in Patient.all:
                if patient.patient_id == patient_index:
                    print(patient)

        # option 3
        elif option == "3":
            patient_name = str(input("Enter patient's name:  "))
            patient_occupation = str(input("Enter patient's occupation:   "))
            patient_condition = str(input("Enter patient's condition:    "))
            new_patient = Patient(
                patient_name, patient_occupation, patient_condition, Patient.count)
            for patient in Patient.all:
                print(patient)

        # option 4
        elif option == "4":
            confirmation = False
            while confirmation == False:
                for patient in Patient.all:
                    print(patient)
                patient_index = int(
                    input("Enter patient ID to remove records of patient:   "))
                confirm = input("Are you sure y/n:   ")
                if confirm == "y":
                    for patient in Patient.all:
                        if patient.patient_id == patient_index:
                            Patient.all.remove(patient)
                            print("Updated Patient List")
                            print("=======================")
                            for patients in Patient.all:
                                # printing what's left in the patient's list
                                print(patients)
                            confirmation = True
                    if confirmation == False:
                        print("There is no one with that ID")
                elif confirm == "n":
                    print("No problem!")
                else:
                    print("Please enter y or n")

        # option 5
        elif option == "5":
            print("Employee List")
            print("=======================")
            for employee in Employee.all:
                print(employee)

        # option 6
        elif option == "6":
            employee_index = int(
                input("Enter employee ID to check records:     "))
            for employee in Employee.all:
                if employee.employee_id == employee_index:
                    print(employee)

        # option 7
        elif option == "7":
            employee_name = str(input("Enter employee's name:  "))
            employee_occupation = str(input("Enter employee's occupation:   "))
            employee_access_level = str(
                input("Enter employee's access level:    "))
            new_employee = Employee(
                employee_name, employee_occupation, employee_access_level, Employee.count)
            for employee in Employee.all:
                print(employee)

        # option 8
        elif option == "8":
            confirmation = False
            while confirmation == False:
                for employee in Employee.all:
                    print(employee)
                employee_index = int(
                    input("Enter employee ID to remove records of employee:   "))
                confirm = input("Are you sure y/n:   ")
                if confirm == "y":
                    for employee in Employee.all:
                        if employee.employee_id == employee_index:
                            Employee.all.remove(employee)
                            print("Updated Employee List")
                            print("=======================")
                            for employees in Employee.all:
                                # printing what's left in the employee's list
                                print(employees)
                            confirmation = True
                    if confirmation == False:
                        print("There is no one with that ID")
                elif confirm == "n":
                    print("No problem!")
                else:
                    print("Please enter y or n")
