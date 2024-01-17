from utils.utils import read_documents
from models.Employee import Employee

class ClientActions:
    def __init__(self, user_manager, user, kms):
        self.user_manager = user_manager
        self.user = user
        self.kms = kms

    def read_documents(self):
        employees = [u for u in self.user_manager.users.values() if isinstance(u, Employee)]
        read_documents(employees)

    def edit_account(self, new_name, new_email, new_password):
        self.kms.update_user_profile(self.user.user_id, name=new_name, email=new_email, password=new_password)

