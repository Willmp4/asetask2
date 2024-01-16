from Authentication import Authentication
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


def read_documents(employees):
    for emp in employees:
        print(f"{emp.name} - {emp.biography.description}")

    employee_name = input("Which employee's biography do you want to read?: ").lower()
    employee = next((emp for emp in employees if emp.name.lower() == employee_name), None)

    if not employee: 
        print("Employee not found")
        return

    print(f"Biography for {employee.name}: {employee.biography.description}")
    for doc in employee.biography.documents:
        print(f"Document: {doc.title}")

    doc_choice = input("Which document do you want to read?: ").lower()
    document = next((doc for doc in employee.biography.documents if doc.title.lower() == doc_choice), None)

    if document:
        print(f"Title: {document.title}\n{document.content}")
    else:
        print("Document not found")

def client_actions(user_manager, user):
    while True:
        print("\n1. View Employee Biographies\n2. Edit Account\n3. Logout")
        choice = input("Enter your choice: ")
        if choice == '1':
            employees = [u for u in user_manager.users.values() if isinstance(u, Employee)]
            read_documents(employees)
        elif choice == '2':
            # Logic for editing client account
            new_name = input("Enter new name: ")
            new_email = input("Enter new email: ")
            new_password = input("Enter new password: ")
            user.update_profile(new_name, new_email, new_password)
            user_manager.save_users()
        elif choice == '3':
            break
        else:
            print("Invalid choice")

def employee_actions(user_manager, user):
    while True:
        print("\n1. Add Document to Biography\n2. Edit Account\n3. Logout")
        choice = input("Enter your choice: ")
        if choice == '1':
            doc_title = input("Enter document title: ")
            doc_content = input("Enter document content: ")
            document = Document(str(uuid.uuid4()), doc_title, doc_content, user.biography.biography_id, None)  # Assuming a constructor for Document
            user.biography.add_document(document)
            print("Document added to your biography")
            user_manager.save_users() # Save changes to the JSON file
        elif choice == '2':
            # Logic for editing employee account
            new_name = input("Enter new name: ")
            new_email = input("Enter new email: ")
            new_password = input("Enter new password: ")
            user.update_profile(new_name, new_email, new_password)
            user_manager.save_users()
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
            user_type = input("Enter user type (employee/client): ").lower()
            # use while loop to check if user_type is valid
            while user_type not in ['employee', 'client']:
                print("Invalid user type")
                user_type = input("Enter user type (employee/client): ").lower()
            
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
                if user.role == "client":
                    client_actions(user_manager, user)
                elif user.role == "employee":
                    employee_actions(user_manager, user)
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
