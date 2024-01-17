from document.Document import Document
from utils.utils import read_documents
from models.Employee import Employee
import uuid

class EmployeeActions:
    def __init__(self, user_manager, user, kms):
        self.user_manager = user_manager
        self.user = user
        self.kms = kms

    def add_document_to_biography(self):
        doc_title = input("Enter document title: ")
        doc_content = input("Enter document content: ")
        document = Document(str(uuid.uuid4()), doc_title, doc_content, self.user.biography.biography_id, None)
        self.kms.add_document_to_biography(self.user.biography.biography_id, document)

    def read_documents(self):
        employees = [u for u in self.user_manager.users.values() if isinstance(u, Employee)]
        read_documents(employees)

    def edit_biography(self):
        new_description = input("Enter new biography description: ")
        self.kms.update_biography(self.user.biography.biography_id, new_description)

    def edit_document(self):
        doc_id = input("Enter document ID to edit: ")
        new_title = input("Enter new document title (leave blank for no change): ")
        new_content = input("Enter new document content (leave blank for no change): ")
        self.kms.update_document_in_biography(self.user.biography.biography_id, doc_id, new_title, new_content)

    def edit_account(self):
        new_name = input("Enter new name: ")
        new_email = input("Enter new email: ")
        new_password = input("Enter new password: ")
        self.kms.update_user_profile(self.user.user_id, name=new_name, email=new_email, password=new_password)
