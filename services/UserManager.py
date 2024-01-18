import json
from models.Employee import Employee, Client
from biography.Biography import Biography
from document.Document import Document


class UserManager:
    def __init__(self, user_dao):
        self.user_dao = user_dao
        self.users = {}
        self.load_users()

    def add_user(self, user):
        self.users[user.user_id] = user
        self.save_users()
    
    def find_user_by_email(self, email):
        return next((user for user in self.users.values() if user.email == email), None)
    
    def find_user_by_id(self, user_id):
        return self.users.get(user_id, None)
    
    def find_biography_by_id(self, biography_id):
        for user in self.users.values():
            if isinstance(user, Employee) and user.biography.biography_id == biography_id:
                return user.biography
        return None

    def load_users(self):
        data = self.user_dao.load_users()
        for user_data in data.get('employees', []):
            biography_data = user_data.pop('biography', None)
            biography = None
            if biography_data:
                documents = [Document(**doc) for doc in biography_data.pop('documents', [])]
                biography = Biography(**biography_data)
                biography.documents = documents

            employee = Employee(biography_description=biography.description ,biography=biography, **user_data,  password_hashed=True)
            self.users[employee.user_id] = employee

        for user_data in data.get('clients', []):
            client = Client(**user_data, password_hashed=True)
            self.users[client.user_id] = client

    def save_users(self):
        data = {
            'employees': [user.to_dict() for user in self.users.values() if isinstance(user, Employee)],
            'clients': [user.to_dict() for user in self.users.values() if isinstance(user, Client)]
        }
        self.user_dao.save_users(data)
