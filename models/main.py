from Authentication import Authentication
from KMS import KnowledgeManagementSystem
from Biography import Biography
from Document import Document
from Employee import Employee, Client
import uuid
import json

def save_to_json(database, filename='database.json'):
    with open(filename, 'w') as file:
        json.dump(database, file, default=lambda o: o.__dict__, indent=4)

def load_from_json(filename='database.json'):
    with open(filename, 'r') as file:
        return json.load(file)

def create_user(database, user_type):
    name = input("Enter name: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    
    if user_type == 'employee':
        employee_id = str(uuid.uuid4())  # Ensure it's converted to a string
        biography = input("Enter biography: ")
        skills = input("Enter skills (comma-separated): ").split(',')
        experience = int(input("Enter experience (years): "))
        role = input("Enter role: ")
        user = Employee.create_user(employee_id, name, role, email, password, biography, skills, experience)
        database['employees'].append(user)
        database['biographies'].append(Biography(employee_id, name, biography, None, None))

    elif user_type == 'client':
        client_id = str(uuid.uuid4())
        company_name = input("Enter company name: ")
        user = Client.create_user(client_id, name, email, password, company_name)
        database['clients'].append(user)

    save_to_json(database)



def employee_actions(kms, user):
    while True:
        print("\n1. Update Profile\n2. Manage Biographies\n3. Logout")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            password = input("Enter password: ")
            kms.update_user_profile(user.user_id, name, email, password)
        elif choice == '2':
            print("\n1. View Biography\n2. Update Biography")
            bio_choice = input("Enter your choice: ")
            if bio_choice == '1':
                print("Biography: ", user.biography)
            elif bio_choice == '2':
                new_bio = input("Enter new biography: ")
                kms.update_employee_biography(user.employee_id, new_bio)
            else:
                print("Invalid choice")
        elif choice == '3':
            break
        else:
            print("Invalid choice")

def client_actions(kms, user):
    while True:
        print("\n1. View Biographies\n2. Access Reports\n3. Logout")
        choice = input("Enter your choice: ")
        if choice == '1':
            employee_id = input("Enter the employee ID to view biography: ")
            # Logic to view biography of the specified employee
            employee = next((emp for emp in kms.database['employees'] if emp.employee_id == employee_id), None)
            if employee:
                print(f"Biography for {employee.name}: {employee.biography}")
            else:
                print("Employee not found")
        elif choice == '2':
            # Access reports logic
            print("Reports feature not implemented yet")
        elif choice == '3':
            break
        else:
            print("Invalid choice")


def main():
    # Load or initialize the database
    try:
        database = load_from_json()
    except FileNotFoundError:
        database = {'users': [], 'employees': [], 'clients': [], 'biographies': []}

    kms = KnowledgeManagementSystem("KMS1", "Knowledge Management System", database)

    while True:
        print("\n1. Create User\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            user_type = input("Enter user type (employee/client): ")
            create_user(database, user_type)
        elif choice == '2':
            email = input("Enter email: ")
            password = input("Enter password: ")
            user = kms.authenticate_user(email, password)
            print(user)
            if user:
                if isinstance(user, Employee):
                    employee_actions(kms, user)
                elif isinstance(user, Client):
                    client_actions(kms, user)
        elif choice == '3':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
