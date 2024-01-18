from models.User import User
class Admin(User):
    def __init__(self, user_id, name, email, password, role="Admin", password_hashed=False):
        super().__init__(user_id, name, role, email, password, password_hashed)
        # Additional admin-specific attributes can be added here

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'role': self.role,
            'email': self.email,
            'password': self.password,
            # Include additional admin-specific attributes here if any
        }

    @staticmethod
    def create_admin(user_id, name, email, password ):
        return Admin(user_id, name, email, password)
