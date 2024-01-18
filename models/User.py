# Purpose: User class for the application
import bcrypt
import re

class User:
    def __init__(self, user_id, name, role, email, password):
        self.user_id = user_id
        self.name = name
        self.role = role
        self.email = email
        self.password = password

    def validate_email(self, email):
        email_regex = r"[^@]+@[^@]+\.[^@]+"
        if re.match(email_regex, email):
            return True
        else:
            return False

    def update_profile(self, name=None, email=None, password=None):
        if name:
            self.name = name
        if email:
            if self.validate_email(email):
                self.email = email
            else:
                print("Invalid email")
        if password:
            self.password = password
        print("Profile updated")

    def set_password(self, password):
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        # Convert the hashed password to a string using decode
        self.password = hashed.decode('utf-8')

    def check_password(self, password):
        # Convert the stored password back to bytes for comparison
        stored_password = self.password.encode('utf-8')
        return bcrypt.checkpw(password.encode('utf-8'), stored_password)


