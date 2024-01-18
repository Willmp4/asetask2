from services.UserManager import UserManager
from services.KMS import KnowledgeManagementSystem
from services.Authentication import Authentication
from commands.Invoker import Invoker
from CommandIssuer import CommandIssuer  
from actions.EmployeeActions import EmployeeActions
from actions.AdminActions import AdminActions 
from actions.ClientActions import ClientActions
from database.JsonUserDAO import JsonUserDAO

def gather_employee_details(name, email, password):
    biography_description = input("Enter biography description: ")
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

def user_flow(command_issuer, user):
    if user.role == "employee":
        employee_menu(command_issuer, user)
    elif user.role == "client":
        client_menu(command_issuer, user)
    elif user.role == "Admin":
        admin_menu(command_issuer, user)


def admin_menu(command_issuer, user):
    while True:
        print("\nAdmin Menu\n----------\n1. View All Biographies\n2. Edit Any Document\n3. Logout")
        choice = input("Enter your choice: ")
        actions = AdminActions(command_issuer.user_manager, user, command_issuer.kms)

        if choice == '1':
            employee_biographies = command_issuer.issue_command('access_all_biographies', actions=actions)
            for name, bio in employee_biographies:
                print(f"\nBiography of {name}")
                print(f"Description: {bio['description']}")
                # Add more details as needed
        elif choice == '2':  # New option for editing any document
            employee_name = input("Enter employee's name to list their documents: ")
            actions = AdminActions(command_issuer.user_manager, user, command_issuer.kms)
            documents = command_issuer.issue_command('list_documents_for_employee', actions=actions, employee_name=employee_name)

            if documents:
                print("Available Documents:")
                for doc_title, _ in documents:
                    print(f"Title: {doc_title}")

                doc_title = input("Enter the title of the document to edit: ")
                new_title = input("Enter new title: ")
                new_content = input("Enter new content: ")
                command_issuer.issue_command('edit_any_document_by_title', actions=actions, employee_name=employee_name, doc_title=doc_title, new_title=new_title, new_content=new_content)
            else:
                print("No documents available or employee not found")
       
        elif choice == '3':
            break  # Logout
        else:
            print("Invalid choice")



def employee_menu(command_issuer, user):
    while True:
        print("\nMain Menu\n---------\n1. Document Management\n2. Biography Management\n3. Account Management\n4. Logout")
        main_choice = input("Select a category: ")

        if main_choice == '1':
            document_management(command_issuer, user)
        elif main_choice == '2':
            biography_management(command_issuer, user)
        elif main_choice == '3':
            account_management(command_issuer, user)
        elif main_choice == '4':
            break  # Logout
        else:
            print("Invalid choice")

def client_menu(command_issuer, user):
    while True:
        print("\nClient Menu\n-----------\n1. View Documents\n2. Edit Account\n3. Logout")
        choice = input("Enter your choice: ")
        actions = ClientActions(command_issuer.user_manager, user, command_issuer.kms)

        if choice == '1':
            command_issuer.issue_command('view_documents', actions=actions)
        elif choice == '2':
            account_management(command_issuer, user)
        elif choice == '3':
            break  # Logout
        else:
            print("Invalid choice")

def document_management(command_issuer, user):
    while True:
        print("\nDocument Management\n-------------------\n1. Add Document to Biography\n2. View Documents\n3. Edit Document\n4. Go Back")
        choice = input("Select an action: ")
        actions = EmployeeActions(command_issuer.user_manager, user, command_issuer.kms)

        if choice == '1':
            doc_title = input("Enter document title: ")
            doc_content = input("Enter document content: ")
            command_issuer.issue_command('add_document', user=user, actions=actions,title=doc_title, content=doc_content)
        elif choice == '2':
            command_issuer.issue_command('view_documents', user=user, actions=actions)
        elif choice == '3':
            documents = command_issuer.issue_command('get_document', user=user, actions=actions)
            if documents:
                print("Available Documents:")
                for doc in documents:
                    print(f"Title: {doc.title}")

            doc_id = input("Enter document title: ")
            new_title = input("Enter new title: ")
            new_content = input("Enter new content: ")
            command_issuer.issue_command('edit_document', actions=actions, user=user, doc_id=doc_id, new_title=new_title, new_content=new_content)
        elif choice == '4':
            break  # Go back to main menu
        else:
            print("Invalid choice")

def biography_management(command_issuer, user):
    while True: 
        print("\nBiography Management\n--------------------\n1. Edit Biography\n2. Go Back")
        choice = input("Select an action: ")
        if choice == '1':
            new_description = input("Enter new description: ")
            command_issuer.issue_command('edit_biography', actions=EmployeeActions(command_issuer.user_manager, user, command_issuer.kms), new_description=new_description)
        elif choice == '2':
            break  # Go back to main menu
        else:
            print("Invalid choice")

def account_management(command_issuer, user):
    while True:
        print("\nAccount Management\n------------------\n1. Edit Account\n2. Go Back")
        choice = input("Select an action: ")
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            while email == '' or '@' not in email or '.' not in email:
                print("Invalid email")
                email = input("Enter email: ")
                
            password = input("Enter password: ")
            if user == 'employee':
                actions = EmployeeActions(command_issuer.user_manager, user, command_issuer.kms)
                command_issuer.issue_command('edit_user', actions=actions, name=name, email=email, password=password)
            else:
                actions = ClientActions(command_issuer.user_manager, user, command_issuer.kms)
                command_issuer.issue_command('edit_user', actions=actions, name=name, email=email, password=password)
        elif choice == '2':
            break  # Go back to main menu
        else:
            print("Invalid choice")


def main():
    user_dao = JsonUserDAO('database/database.json')
    user_manager = UserManager(user_dao)
    kms = KnowledgeManagementSystem("KmsV1", "KMS", user_manager)
    authenticator = Authentication(user_manager)
    invoker = Invoker()
    command_issuer = CommandIssuer(invoker, user_manager, kms)  # Create a CommandIssuer instance

    while True:
        choice = input("\n1. Create User\n2. Login\n3. Exit\nEnter your choice: ")
        if choice == '1':
            user_type = input("Enter user type (employee/client): ").lower()
            if user_type not in ['employee', 'client', 'admin']:
                print("Invalid user type")
                continue
            name = input("Enter name: ")
            #validate email
            email = input("Enter email: ")
            while email == '' or '@' not in email or '.' not in email:
                print("Invalid email")
                email = input("Enter email: ")

            password = input("Enter password: ")

            if user_type == 'employee':
                additional_params = gather_employee_details(name, email, password)
            elif user_type == 'client':
                additional_params = gather_client_details(name, email, password)
            else:
                additional_params = {'name': name, 'email': email, 'password': password}
            command_issuer.issue_command('create_user',user_type=user_type, **additional_params)  

        elif choice == '2':
            email = input("Enter email: ")
            password = input("Enter password: ")
            user = command_issuer.issue_command('login_user', authenticator=authenticator, email=email, password=password)
            if user:
                user_flow(command_issuer, user)
            else:
                print("Login failed")
        elif choice == '3':
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
