import json
from database.UserDAOInterface import UserDAOInterface

class JsonUserDAO(UserDAOInterface):
    def __init__(self, filename):
        self.filename = filename

    def load_users(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_users(self, users):
        with open(self.filename, 'w') as file:
            json.dump(users, file, indent=4)
