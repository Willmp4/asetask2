from models.Employee import Employee
from models.Client import Client
from models.Admin import Admin
import uuid

class KnowledgeManagementSystem:
    def __init__(self, system_id, name, database):
        self.system_id = system_id
        self.name = name
        self.database = database
                
    def provide_access(self, user):
        if user.role == "client":
            print("Client access granted")
        elif user.role == "employee":
            print("Employee access granted")
        else:
            print("Access denied")
    
    def update_employee_biography(self, employee_id, biography_data):
        for employee in self.database['employees']:
            if employee.employee_id == employee_id:
                employee.biography.update_biography_info(**biography_data)
                print("Biography updated")
                return
        print("Employee not found")

    def add_user(self, user):
        self.database.add_user(user)
    
    def create_user(self, user_type, **kwargs):
        if user_type == 'employee':
            user = Employee(str(uuid.uuid4()), **kwargs)
        elif user_type == 'client':
            user = Client(str(uuid.uuid4()), **kwargs)
        elif user_type == 'admin':
            user = Admin(str(uuid.uuid4()), **kwargs)
        else:
            raise ValueError("Invalid user type")
        self.add_user(user)
        print("User created and added to the system")

    def update_user_profile(self, user_id, **kwargs):
        user = self.database.find_user_by_id(user_id)
        if user:
            user.update_profile(**kwargs)
            self.database.save_users()
            print("User profile updated")
        else:
            print("User not found")

    def add_document_to_biography(self, biography_id, document):
        biography = self.database.find_biography_by_id(biography_id)
        if biography:
            biography.add_document(document)
            self.database.save_users()
            print("Document added to biography")
        else:
            print("Biography not found")

    def update_biography(self, biography_id, new_description):
        biography = self.database.find_biography_by_id(biography_id)
        if biography:
            biography.description = new_description  # assuming biography has a 'description' attribute
            self.database.save_users()
            print("Biography updated successfully")
        else:
            print("Biography not found")

    def update_document_in_biography(self, biography_id, document_id, new_title=None, new_content=None):
        biography = self.database.find_biography_by_id(biography_id)
        if biography:
            document = next((doc for doc in biography.documents if doc.title == document_id), None)
            if document:
                if new_title:
                    document.title = new_title
                if new_content:
                    document.content = new_content
                self.database.save_users()
                print("Document updated successfully")
            else:
                print("Document not found")
        else:
            print("Biography not found")