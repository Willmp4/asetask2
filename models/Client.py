#This is the Client class that inherits from the User class
from models.User import User
class Client(User):

    def __init__(self, user_id, name, email, password, company_name, role="client", password_hashed=False):
        super().__init__(user_id, name, role, email, password, password_hashed)
        self.company_name = company_name
        self.company_name = company_name
        if not password_hashed:
            self.set_password(password)
        else:
            self.password = password
    

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'role': self.role,
            'email': self.email,
            'password': self.password,
            'company_name': self.company_name
        }


    @staticmethod
    def create_user( user_id, name, email, password, company_name, ):
        return Client( user_id, name, email, password, company_name)


