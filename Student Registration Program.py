import csv

 # importing random so we can generate a random student id for each student and coupon numbers

import random

# Importing OS so I can check if our csv file exists

from os import path

# Defining a student manager class with read, write, authenticate and update methods

class StudentManager:
    
    # Loads student information from the specified filename

    def __init__(self, csv_filename):
        self.csv_filename = csv_filename
        self.students = self.load_students()

    def load_students(self):
        students = []
        with open(self.csv_filename, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                try:
                    row['Balance'] = float(row['Balance'])
                except ValueError:
                    print(f"Error converting 'Balance' to float for student ID {row['Student ID']}")
                students.append(row)
        return students
    
    # Authentication for specific student

    def authenticate(self, student_id, password):
        for student in self.students:
            if student['Student ID'] == student_id and student['Password'] == password:
                return True
        return False

    # Update method to update all the info throughout the program

    def update_student_info(self, student_id, new_data):
        for student in self.students:
            if student['Student ID'] == student_id:
                for key, value in new_data.items():
                    student[key] = value
                break

    # Writes back to the csv file with error handling 

    def write_to_csv(self):
        try:
            with open(self.csv_filename, 'w', newline='') as file:
                fieldnames = ['Name', 'Age', 'Phone Number', 'Email', 'Password', 'Student ID', 'Balance', 'Module 1', 'Module 2']
                csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
                csv_writer.writeheader()
                csv_writer.writerows(self.students)
        except (PermissionError, OSError) as e:
            print(f"Error writing to CSV: {e}")

# Defining our student class with information about the student

class Student:
    def __init__(self, data):
        self.name = data['Name']
        self.age = data['Age']
        self.number = data['Phone Number']
        self.email = data['Email']
        self.password = data['Password']
        self.student_id = data['Student ID']
        self.balance = data['Balance']
        self.mod1 = data['Module 1']
        self.mod2 = data['Module 2']

def student_regi():

    # Gathering information from the user

    name = input("Please enter your name: ")
    age = input("Please enter your age: ")
    while True:
        try:
            num = int(input("Please enter your phone number: "))
            break
        except ValueError:
            print("Please enter a valid number!")
    email = input("Please enter your email address: ")
    password = input("Please create a password: ")
    stud_id = int(random.randint(1,10001))
    student_balance = float(400)
    mod1 = 'N/A'
    mod2 = 'N/A'
    print(f"Your student ID is: {stud_id}")

    new_dict = {'Name': name, 'Age': age, 'Phone Number': num, 'Email': email, 'Password': password, 'Student ID': stud_id, 
                'Balance': student_balance, 'Module 1': mod1, 'Module 2': mod2}
    
    # Appends new entries to the csv file

    colnames = ['Name', 'Age', 'Phone Number', 'Email', 'Password', 'Student ID', 'Balance', 'Module 1', 'Module 2']

    with open('student_details.csv', 'a', newline='') as csv_file:
        dictwrt = csv.DictWriter(csv_file, fieldnames=colnames)
        dictwrt.writerow(new_dict)

    



    
def module_selection():

     # Going through the authentication process

    student_id = input("Please enter your student ID: ")
    password = input("Please enter your password: ")

    # Tells the student manager class which file to read from

    student_manager = StudentManager('student_details.csv')

    # Assumes we want to edit the first entry in the csv file and given the user is authenticated, 

    if student_manager.authenticate(student_id, password):
        print("User authenticated")

        student_instance = Student(student_manager.students[0])

    # Checks if the student has already gone through the selection process first 

        if student_instance.mod1 != "N/A" and student_instance.mod2 != "N/A":
            print("You have already selected your modules!")
        else:
            try:
                selection1 = input("\n Please select your first module: \n1. Programming 1\n2. Programming 2\n3. Networking 1\n4. Networking 2")
            except ValueError:
                print("Please enter a valid number!")
            if selection1 == '1':
                student_instance.mod1 = 'Programming 1'
                try:
                    selection2 = input("\n PLease select your second module: \n2. Programming 2\n3. Networking 1\n4. Networking 2")
                except ValueError:
                    print("Please enter a valid number!")
                if selection2 == '2':
                    student_instance.mod2 = 'Programming 2'
                elif selection2 == '3':
                    student_instance.mod2 = 'Networking 1'
                elif selection2 == '4':
                    student_instance.mod2 = 'Networking 2'
            
            elif selection1 == '2':
                student_instance.mod1 = 'Programming 2'
                try:
                    selection2 = input("\n PLease select your second module: \n1. Programming 1\n3. Networking 1\n4. Networking 2")
                except ValueError:
                    print("Please enter a valid number!")
                if selection2 == '1':
                    student_instance.mod2 = 'Programming 1'
                elif selection2 == '3':
                    student_instance.mod2 = 'Networking 1'
                elif selection2 == '4':
                    student_instance.mod2 = 'Networking 2'

            elif selection1 == '3':
                student_instance.mod1 = 'Networking 1'
                try:
                    selection2 = input("\n PLease select your second module: \n1. Programming 1\n2. Programming 2\n4. Networking 2")
                except ValueError:
                    print("Please enter a valid number!")
                if selection2 == '1':
                    student_instance.mod2 = 'Programming 1'
                elif selection2 == '2':
                    student_instance.mod2 = 'Programming 2'
                elif selection2 == '4':
                    student_instance.mod2 = 'Networking 2'

            elif selection1 == '4':
                student_instance.mod1 = 'Networking 2'
                try:
                    selection2 = input("\n PLease select your second module: \n1. Programming 1\n2. Programming 2\n3. Networking 1")
                except ValueError:
                    print("Please enter a valid number!")
                if selection2 == '1':
                    student_instance.mod2 = 'Programming 1'
                elif selection2 == '2':
                    student_instance.mod2 = 'Programming 2'
                elif selection2 == '3':
                    student_instance.mod2 = 'Networking 1'

            print(f"Your selected modules are: ", student_instance.mod1, student_instance.mod2)
   
    else:
        print("Access Denied")
        return
    
    student_manager.update_student_info(student_instance.student_id, {'Module 1': student_instance.mod1})
    student_manager.update_student_info(student_instance.student_id, {'Module 2': student_instance.mod2})
    student_manager.write_to_csv()


def shopping():

    # Going through the authentication process

    student_id = input("Please enter your student ID: ")
    password = input("Please enter your password: ")

    # Tells the student manager class which file to read from

    student_manager = StudentManager('student_details.csv')

    # Assumes we want to edit the first entry in the csv file and given the user is authenticated, 
    # it goes through the shopping cycle

    if student_manager.authenticate(student_id, password):
        print("User authenticated")

        student_instance = Student(student_manager.students[0])

        total_of_p = 0  # Initialize print paper cost
        total_of_f = 0  # Initialize food cost

        while True:

                choice = input("\nWhat would you like to buy?(Or d if finished shopping)\n1. Print paper\n2.Food")

                if choice == 'd':
                    break
                elif choice == '1':
                    num_of_p = float(input("\nHow many pages would you like to print?: "))
                    total_of_p = num_of_p * 1.25
                elif choice == '2':
                    num_of_f = float(input("\nHow many portions of food would you like?: "))
                    total_of_f = num_of_f * 7.5

        total_cost = total_of_p + total_of_f

        if total_cost <= student_instance.balance:
            coupon = float(random.randint(0,51))
            up_bal = (student_instance.balance - total_cost) + coupon
            student_instance.balance = up_bal
            student_manager.update_student_info(student_id, {'Balance': up_bal})
            print(f"Your total cost is: {total_cost},your new balance is ", student_instance.balance)
            print(f"and you earned a coupon worth {coupon}!, This was added to your balance.")
        elif total_cost >= student_instance.balance:
            print("You do not have enough to purchase these items!")
        else:
            print("Access Denied")
            return
        
        # Writing back to csv

        student_manager.write_to_csv()


def student_account():
    
    # Going through the authentication process

    student_id = input("Please enter your student ID: ")
    password = input("Please enter your password: ")

    # Tells the student manager class which file to read from

    student_manager = StudentManager('student_details.csv')

    # Assumes we want to edit the first entry in the csv file and given the user is authenticated, 
    # it goes through the update cycle

    if student_manager.authenticate(student_id, password):
        print("User authenticated")

        student_instance = Student(student_manager.students[0])

        # Going through the balance add and confirm

        add_balance = float(input("\nHow many points would you like to add: "))
        confirm = input(f"Confirm to add {add_balance} to your account (y/n): ")

        # Updating balance based on previous user input

        if confirm == 'y':
            new_balance = student_instance.balance + add_balance
            student_instance.balance = new_balance
            student_manager.update_student_info(student_id, {'Balance': new_balance})
            print("Your new balance is: ", student_instance.balance)
        elif confirm == 'n':
            print("Returning to main page!")     
    else:
        print("Access Denied")

        #Writing back to csv

        student_manager.write_to_csv()

def check_bal():

    #Authenticates the user

    student_id = input("Please enter your student ID: ")
    password = input("Please enter your password: ")

    # Tells the student manager class which file to read from

    student_manager = StudentManager('student_details.csv')

    # Assumes we want to edit the first entry in the csv file and given the user is authenticated, 
    # it goes through the show balance 

    if student_manager.authenticate(student_id, password):
        print("User authenticated")

        student_instance = Student(student_manager.students[0])

        print("\nYour balance is:", student_instance.balance)
    
    else:
        print("Access Denied")
        return

        
                   
def edit_info():

    #Authenticates the user

    student_id = input("Please enter your student ID: ")
    password = input("Please enter your password: ")

    # Tells the student manager class which file to read from

    student_manager = StudentManager('student_details.csv')

    # Assumes we want to edit the first entry in the csv file and given the user is authenticated, 
    # it goes through the update cycle

    if student_manager.authenticate(student_id, password):
        print("User authenticated")

        student_instance = Student(student_manager.students[0])

        while True:

            choice = input("\n Please choose what you would like to edit (Or q to exit): \n1. Email \n2. Phone number \n3. Password")

            if choice == 'q':
                break
            elif choice == '1':
                new_email = input("\nPlease enter your new email: ")
                student_instance.email = new_email
                student_manager.update_student_info(student_id, {'Email': new_email}) 

            elif choice == '2':
                while True:
                    try:
                        new_number = int(input("\nPlease enter your new phone number: "))
                        student_instance.number = new_number
                        student_manager.update_student_info(student_id, {'Phone Number': new_number})
                        break
                    except ValueError:
                        print("Please enter a valid number!")
            elif choice == '3':
                new_password = input("\nPlease enter your new password: ")
                student_instance.password = new_password
                student_manager.update_student_info(student_id, {'Password': new_password})

            else:
                print("Access denied")
                break

            # Writes our updates back to the csv file
                
            student_manager.write_to_csv()

def reporting():

    #Authenticates the user

    student_id = input("Please enter your student ID: ")
    password = input("Please enter your password: ")

    # Tells the student manager class which file to read from

    student_manager = StudentManager('student_details.csv')

    # Assumes we want to edit the first entry in the csv file and given the user is authenticated, 
    # it goes through the show info cycle

    if student_manager.authenticate(student_id, password):
        print("User authenticated")

        student_instance = Student(student_manager.students[0])

        print("Your details are:", "Name:",student_instance.name,"Age:", student_instance.age,"Phone Number:", student_instance.number,
              "Email:", student_instance.email,"Student ID:", student_instance.student_id,"Balance:", student_instance.balance,
              'Module 1:', student_instance.mod1, 'Module 2:', student_instance.mod2)
        
    else:
        print("Access Denied")
        return


# Creating the main page 

# Checking if file exists

file_path = 'student_details.csv'

# If it does the program loads the student loader method that reads the file

if path.exists(file_path):
    StudentManager(file_path)

else:
    
    # Creating a csv file for us to later read and write to

    colnames = ['Name', 'Age', 'Phone Number', 'Email', 'Password', 'Student ID', 'Balance', 'Module 1', 'Module 2']

    with open('student_details.csv', 'w', newline='') as csv_file:
        wrt = csv.writer(csv_file)
        wrt.writerow(colnames)

while True:
    print("\nWelcome to the self-service student registration program!")
    print("\n1. Student registration\n2. Module selection and verification\n3. Student account top-up\n4. Shopping\n5. Check balance\n6. Edit informaiton\n7. Reporting")

    

    choice = input("\nPlease Choose what page you would like to view (Or q to exit): ")

    if choice == "q":
        print("Thank you for using the student registration!")
        break
    elif choice == "1":
            student_regi()
    elif choice == "2":
            module_selection()
    elif choice == "3":
            student_account()
    elif choice == "4":
            shopping()
    elif choice == "5":
            check_bal()
    elif choice == "6":
            edit_info()
    elif choice == "7":
            reporting()


