from Authentication import Authentication
from KMS import KnowledgeManagementSystem
from Biography import Biography
from Document import Document
from Employee import Employee, Client
from UserManager import UserManager
from Authentication import Authentication
import uuid
import json

def create_user(user_manager, user_type):
    name = input("Enter name: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    
    if user_type == 'employee':
        employee_id = str(uuid.uuid4())
        biography_description = input("Enter biography: ")
        skills = input("Enter skills (comma-separated): ").split(',')
        experience = int(input("Enter experience (years): "))
        role = user_type
        user = Employee(employee_id, name, role, email, password, biography_description, skills, experience)
    elif user_type == 'client':
        client_id = str(uuid.uuid4())
        company_name = input("Enter company name: ")
        user = Client(client_id, name, email, password, company_name)
    else:
        raise ValueError("Invalid user type")

    user_manager.add_user(user)

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
    user_manager = UserManager()
    authenticator = Authentication(user_manager)

    while True:
        choice = input("\n1. Create User\n2. Login\n3. Exit\nEnter your choice: ")
        if choice == '1':
            user_type = input("Enter user type (employee/client): ")
            create_user(user_manager, user_type)
        elif choice == '2':
            email = input("Enter email: ")
            password = input("Enter password: ")
            if authenticator.verify_login(email, password):
                user = user_manager.find_user_by_email(email)
                # Assuming login_time and logout_time are provided or calculated
                login_time = None
                logout_time = None  # You can update this when the user logs out
                authenticator.record_session(user.user_id, login_time, logout_time)
                print("Login successful for:", user.name)
                # Further actions based on user type (employee/client)
            else:
                print("Login failed")
        elif choice == '3':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
