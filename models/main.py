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

def client_actions(user_manager, user):
    while True:
        print("\n1. View Employee Biographies\n2. Edit Account\n3. Logout")
        choice = input("Enter your choice: ")
        if choice == '1':
            employees = [u for u in user_manager.users.values() if isinstance(u, Employee)]
            for emp in employees:
                print(f"{emp.employee_id}: {emp.name} - {emp.biography}")

            read_choice = input("Do you want to read a biography? (yes/no): ")
            if read_choice.lower() == 'yes':
                employee_id = input("Enter the employee ID to view biography: ")
                employee = next((emp for emp in employees if emp.employee_id == employee_id), None)
                if employee:
                    print(f"Biography for {employee.name}: {employee.biography}")
                    # Assuming each biography has a list of documents
                    for doc in employee.biography.documents:
                        print(f"Document: {doc.title}")
                else:
                    print("Employee not found")

        elif choice == '2':
            # Logic for editing client account
            pass

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
            pass

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
