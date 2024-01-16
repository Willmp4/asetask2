from Authentication import Authentication
from UserManager import UserManager
from Authentication import Authentication
from KMS import KnowledgeManagementSystem
from UserComands import CreateUserCommand, LoginUserCommand, UpdateUserProfileCommand       
from EmployeeActions import EmployeeActions
from ClientActions import ClientActions
from BiographyComands import AddDocumentToBiographyCommand, ReadBiographyCommand

def gather_employee_details(name, email, password):
    biography_description = input("Enter biography: ")
    skills = input("Enter skills (comma-separated): ").split(',')
    experience = int(input("Enter experience (years): "))
    role = "employee"
    return {
        "name": name,
        "role": role,
        "email": email,
        "password": password,
        "biography_description": biography_description,
        "skills": skills,
        "experience": experience
    }

def gather_client_details(name, email, password):
    company_name = input("Enter company name: ")
    return {
        "name": name,
        "email": email,
        "password": password,
        "company_name": company_name
    }


def handle_add_document(user, kms):
    doc_title = input("Enter document title: ")
    doc_content = input("Enter document content: ")
    command = AddDocumentToBiographyCommand(kms, user, doc_title, doc_content)
    command.execute()

def handle_edit_account(user, kms):
    new_name = input("Enter new name: ")
    new_email = input("Enter new email: ")
    new_password = input("Enter new password: ")
    command = UpdateUserProfileCommand(kms, user.user_id, new_name, new_email, new_password)
    command.execute()

def handle_view_documents(actions):
    command = ReadBiographyCommand(actions)
    command.execute()

def print_menu(role):
    if role == "employee":
        print("\n1. Add Document to Biography\n2. View Documents\n3. Edit Account\n4. Logout")
    else:
        print("\n1. View Documents\n2. Edit Account\n3. Logout")


def user_flow(user, user_manager, kms):
    employee_actions = {
        '1': lambda: handle_add_document(user, kms),
        '2': lambda: handle_view_documents(EmployeeActions(user_manager, user, kms)),
        '3': lambda: handle_edit_account(user, kms)
    }

    client_actions = {
        '1': lambda: handle_view_documents(ClientActions(user_manager, user, kms)),
        '2': lambda: handle_edit_account(user, kms)
    }

    actions = employee_actions if user.role == "employee" else client_actions

    while True:
        print_menu(user.role)
        choice = input("Enter your choice: ")
        action = actions.get(choice)

        if action:
            action()
        elif choice == '4' and user.role == "employee" or choice == '3' and user.role == "client":
            break # Logging out
        else:
            print("Invalid choice")




def main():
    user_manager = UserManager()
    kms = KnowledgeManagementSystem("KmsV1", "KMS", user_manager)
    authenticator = Authentication(user_manager)

    while True:
        choice = input("\n1. Create User\n2. Login\n3. Exit\nEnter your choice: ")
        if choice == '1':
            user_type = input("Enter user type (employee/client): ").lower()
            if user_type not in ['employee', 'client']:
                print("Invalid user type")
                continue
            name = input("Enter name: ")
            email = input("Enter email: ")
            password = input("Enter password: ")

            if user_type == 'employee':
                # Gather additional employee details
                additional_params = gather_employee_details(name, email, password)
            elif user_type == 'client':
                # Gather additional client details
                additional_params = gather_client_details(name, email, password)

            create_user_command = CreateUserCommand(kms, user_type, **additional_params)
            create_user_command.execute()

        elif choice == '2':
            email = input("Enter email: ")
            password = input("Enter password: ")
            login_command = LoginUserCommand(authenticator, email, password)
            user = login_command.execute()
            if user:
                user_flow(user, user_manager, kms)
            else:
                print("Login failed")
        elif choice == '3':
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
