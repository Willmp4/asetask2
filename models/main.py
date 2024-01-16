from Authentication import Authentication
from Document import Document
from Employee import Employee, Client
from UserManager import UserManager
from Authentication import Authentication
from KMS import KnowledgeManagementSystem
import uuid
from EmployeeActions import EmployeeActions
from ClientActions import ClientActions

def create_user(kms, user_type):
    name = input("Enter name: ")
    email = input("Enter email: ")
    password = input("Enter password: ")

    if user_type == 'employee':
        biography_description = input("Enter biography: ")
        skills = input("Enter skills (comma-separated): ").split(',')
        experience = int(input("Enter experience (years): "))
        role = user_type
        kms.create_user(user_type, name=name, role=role, email=email, password=password, biography_description=biography_description, skills=skills, experience=experience)
    elif user_type == 'client':
        company_name = input("Enter company name: ")
        kms.create_user(user_type, name=name, email=email, password=password, company_name=company_name)
    else:
        raise ValueError("Invalid user type")


def main():
    user_manager = UserManager()
    kms = KnowledgeManagementSystem("KmsV1","KMS", user_manager)
    authenticator = Authentication(user_manager)

    while True:
        choice = input("\n1. Create User\n2. Login\n3. Exit\nEnter your choice: ")
        if choice == '1':
            user_type = input("Enter user type (employee/client): ").lower()
            while user_type not in ['employee', 'client']:
                print("Invalid user type")
                user_type = input("Enter user type (employee/client): ").lower()
            create_user(kms, user_type)
        elif choice == '2':  # Assuming this is the login section
            email = input("Enter email: ")
            password = input("Enter password: ")
            if authenticator.verify_login(email, password):
                user = user_manager.find_user_by_email(email)
                if user.role == "client":
                    client_actions = ClientActions(user_manager, user, kms)
                    while True:
                        print("\n1. View Employee Biographies\n2. Edit Account\n3. Logout")
                        action_choice = input("Enter your choice: ")
                        if action_choice == '1':
                            client_actions.view_employee_biographies()
                        elif action_choice == '2':
                            client_actions.edit_account()
                        elif action_choice == '3':
                            break
                        else:
                            print("Invalid choice")
                elif user.role == "employee":
                    employee_actions = EmployeeActions(user_manager, user, kms)
                    while True:
                        print("\n1. Add Document to Biography\n2. Read Documents\n3. Edit Account\n4. Logout")
                        action_choice = input("Enter your choice: ")
                        if action_choice == '1':
                            employee_actions.add_document_to_biography()
                        elif action_choice == '2':
                            employee_actions.read_documents()
                        elif action_choice == '3':
                            employee_actions.edit_account()
                        elif action_choice == '4':
                            break
                        else:
                            print("Invalid choice")
                else:
                    print("Invalid user type")
            else:
                print("Login failed")
        elif choice == '3':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
