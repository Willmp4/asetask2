from Authentication import Authentication
from UserManager import UserManager
from Authentication import Authentication
from KMS import KnowledgeManagementSystem
from UserComands import CreateUserCommand, LoginUserCommand
from EmployeeActions import EmployeeActions
from ClientActions import ClientActions
from BiographyComands import AddDocumentToBiographyCommand

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


def user_flow(user, user_manager, kms):
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
                doc_title = input("Enter document title: ")
                doc_content = input("Enter document content: ")
                add_doc_command = AddDocumentToBiographyCommand(kms, user, doc_title, doc_content)
                add_doc_command.execute()
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


def main():
    user_manager = UserManager()
    kms = KnowledgeManagementSystem("KmsV1", "KMS", user_manager)
    authenticator = Authentication(user_manager)

    while True:
        choice = input("\n1. Create User\n2. Login\n3. Exit\nEnter your choice: ")
        if choice == '1':
            # Here, we need to gather user data first as it's interactive
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
