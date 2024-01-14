class User:
    def __init__(self, user_id, name, role, email, password):
        self.user_id = user_id
        self.name = name
        self.role = role
        self.email = email
        self.password = password

    def update_profile(self, name=None, email=None, password=None):
        if name:
            self.name = name
        if email:
            self.email = email
        if password:
            self.password = password
        print("Profile updated")


