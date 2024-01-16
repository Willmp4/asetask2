from Authentication import Authentication
from Document import Document
from Employee import Employee, Client
from UserManager import UserManager
from Authentication import Authentication
from KMS import KnowledgeManagementSystem
import uuid

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

def client_actions(user_manager, user, kms):
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
            kms.update_user_profile(user.user_id, name=new_name, email=new_email, password=new_password)
        elif choice == '3':
            break
        else:
            print("Invalid choice")

def employee_actions(user_manager, user, kms):
    while True:
        print("\n1. Add Document to Biography\n2. Read Documents\n3. Edit Account\n3. Logout")
        choice = input("Enter your choice: ")
        if choice == '1':
            doc_title = input("Enter document title: ")
            doc_content = input("Enter document content: ")
            document = Document(str(uuid.uuid4()), doc_title, doc_content, user.biography.biography_id, None)  # Assuming a constructor for Document
            kms.add_document_to_biography(user.biography.biography_id, document)
        elif choice == '2':
            employees = [u for u in user_manager.users.values() if isinstance(u, Employee)]
            read_documents(employees)
        elif choice == '3':
            # Logic for editing employee account
            new_name = input("Enter new name: ")
            new_email = input("Enter new email: ")
            new_password = input("Enter new password: ")
            kms.update_user_profile(user.user_id, name=new_name, email=new_email, password=new_password)

        elif choice == '4':
            break
        else:
            print("Invalid choice")

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
                    client_actions(user_manager, user, kms)
                elif user.role == "employee":
                    employee_actions(user_manager, user, kms)
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
