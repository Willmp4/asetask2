from document.Document import Document
from utils.utils import read_documents
from models.Employee import Employee
import uuid
#This is the EmployeeActions class
#This class is used to define the actions that an employee can perform
#The employee can add documents, read documents, edit their biography, edit their documents and edit their account
class EmployeeActions:
    def __init__(self, user_manager, user, kms):
        self.user_manager = user_manager
        self.user = user
        self.kms = kms

    def add_document(self, title, content):
        self.kms.add_document_to_biography(self.user.biography.biography_id, Document(str(uuid.uuid4()), title, content, self.user.biography.biography_id, None))

    def get_user_documents(self):
        return self.user.biography.documents
    
    def read_documents(self):
        employees = [u for u in self.user_manager.users.values() if isinstance(u, Employee)]
        read_documents(employees)

    def edit_biography(self, new_description):
        self.kms.update_biography(self.user.biography.biography_id, new_description)

    def edit_document(self, doc_id, new_title, new_content):
        self.kms.update_document_in_biography(self.user.biography.biography_id, doc_id, new_title, new_content)

    def edit_account(self, **kwargs):
        self.kms.update_user_profile(self.user.user_id, **kwargs)
