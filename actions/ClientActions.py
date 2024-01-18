from utils.utils import read_documents
from models.Employee import Employee
#This is the ClientActions class
#This class is used to define the actions that a client can perform
#The client can read documents and edit their account
class ClientActions:
    def __init__(self, user_manager, user, kms):
        self.user_manager = user_manager
        self.user = user
        self.kms = kms

    def read_documents(self):
        employees = [u for u in self.user_manager.users.values() if isinstance(u, Employee)]
        read_documents(employees)

    def edit_account(self, **kwargs):
        self.kms.update_user_profile(self.user.user_id, **kwargs)

