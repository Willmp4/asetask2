from services.Authentication import Authentication
from services.UserManager import UserManager
from services.Authentication import Authentication
from services.KMS import KnowledgeManagementSystem
from commands.UserComands import CreateUserCommand, LoginUserCommand, UpdateUserProfileCommand       
from actions.EmployeeActions import EmployeeActions
from actions.ClientActions import ClientActions
from commands.BiographyComands import AddDocumentToBiographyCommand, ReadBiographyCommand, UpdateBiographyCommand, UpdateDocumentCommand
from commands.Invoker import Invoker


def gather_employee_details(name, email, password):
    biography_description = input("Enter biography: ")
    skills = input("Enter skills (comma-separated): ").split(',')
    while True:
        try:
            experience = int(input("Enter experience (years): "))
            break
        except ValueError:
            print("Invalid experience")
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


def handle_add_document(invoker, actions):
    doc_title = input("Enter document title: ")
    doc_content = input("Enter document content: ")
    command = AddDocumentToBiographyCommand(actions, doc_title, doc_content)
    invoker.store_and_execute(command)

def handle_edit_account(invoker, actions):
    new_name = input("Enter new name: ")
    new_email = input("Enter new email: ")
    new_password = input("Enter new password: ")
    command = UpdateUserProfileCommand(actions, name=new_name, email=new_email, password=new_password)
    invoker.store_and_execute(command)

def handle_view_documents(invoker, actions):
    command = ReadBiographyCommand(actions)
    invoker.store_and_execute(command)

def handle_edit_biography(invoker, actions):
    new_description = input("Enter new biography description: ")
    command = UpdateBiographyCommand(actions, new_description)
    invoker.store_and_execute(command)

def handle_edit_document(user, invoker, actions):
    for doc in user.biography.documents:
        print(doc.title)
    doc_id = input("Enter document ID to edit: ")
    new_title = input("Enter new document title (leave blank for no change): ")
    new_content = input("Enter new document content (leave blank for no change): ")

    command = UpdateDocumentCommand(actions, doc_id, new_title, new_content)
    invoker.store_and_execute(command)

def employee_menu(invoker, user, user_manager, kms):
    while True:
        print("\nMain Menu\n---------\n1. Document Management\n2. Biography Management\n3. Account Management\n4. Logout")
        main_choice = input("Select a category: ")

        actions = EmployeeActions(user_manager, user, kms)

        if main_choice == '1':
            document_management(invoker, user, actions)
        elif main_choice == '2':
            biography_management(invoker, actions)
        elif main_choice == '3':
            account_management(invoker, actions)
        elif main_choice == '4':
            break  # Logout
        else:
            print("Invalid choice")

def document_management(invoker, user, actions):
    while True:
        print("\nDocument Management\n-------------------\n1. Add Document to Biography\n2. View Documents\n3. Edit Document\n4. Go Back")
        choice = input("Select an action: ")

        if choice == '1':
            handle_add_document(invoker, actions)
        elif choice == '2':
            handle_view_documents(invoker, actions)
        elif choice == '3':
            handle_edit_document(invoker, user, actions)
        elif choice == '4':
            break  # Go back to main menu
        else:
            print("Invalid choice")

def biography_management(invoker, actions):
    while True:

        print("\nBiography Management\n--------------------\n1. Edit Biography\n2. Go Back")
        choice = input("Select an action: ")
        if choice == '1':
            handle_edit_biography(invoker, actions)
        elif choice == '2':
            break  # Go back to main menu
        else:
            print("Invalid choice")

def account_management(invoker, actions):
    while True:
        print("\nAccount Management\n------------------\n1. Edit Account\n2. Go Back")
        choice = input("Select an action: ")
        if choice == '1':
            handle_edit_account(invoker, actions)
        elif choice == '2':
            break  # Go back to main menu
        else:
            print("Invalid choice")

def user_flow(invoker, user, user_manager, kms):
    if user.role == "employee":
        employee_menu(invoker, user, user_manager, kms)
    elif user.role == "client":
        actions = ClientActions(user_manager, user, kms)
        client_actions = {
            '1': lambda: handle_view_documents(invoker, actions),
            '2': lambda: handle_edit_account(invoker, actions)
        }
        while True:
            print("\nClient Menu\n-----------\n1. View Documents\n2. Edit Account\n3. Logout")
            choice = input("Enter your choice: ")
            action = client_actions.get(choice)
            if action:
                action()
            elif choice == '3':
                break  # Logging out
            else:
                print("Invalid choice")


def main():
    user_manager = UserManager()
    kms = KnowledgeManagementSystem("KmsV1", "KMS", user_manager)
    authenticator = Authentication(user_manager)
    invoker = Invoker()

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
                user_flow(invoker, user, user_manager, kms)
            else:
                print("Login failed")
        elif choice == '3':
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
