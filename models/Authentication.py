class Authentication:
    def __init__(self, auth_id, login_time, logout_time, user_id):
        self.auth_id = auth_id
        self.login_time = login_time
        self.logout_time = logout_time
        self.user_id = user_id

    def verify_login(self, email, password, db):
        user = next((u for u in db['users'] if u.email == email and u.password == password), None)
        return user is not None

    def record_session(self, login_time, logout_time, db):
        self.login_time = login_time
        self.logout_time = logout_time
        db['sessions'].append(self)
        print("Session recorded")