import json
from Employee import Employee, Client

class UserManager:
    def __init__(self, filename='database.json'):
        self.filename = filename
        self.users = {}
        self.load_users()

    def add_user(self, user):
        self.users[user.user_id] = user
        self.save_users()
    
    def find_user_by_email(self, email):
        return next((user for user in self.users.values() if user.email == email), None)

    
    def load_users(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                for user_data in data.get('employees', []):
                    self.add_user(Employee(**user_data))
                for user_data in data.get('clients', []):
                    self.add_user(Client(**user_data))
        except FileNotFoundError:
            pass


    def save_users(self):
        data = {
            'employees': [user.to_dict() for user in self.users.values() if isinstance(user, Employee)],
            'clients': [user.to_dict() for user in self.users.values() if isinstance(user, Client)]
        }
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)