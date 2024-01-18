class Authentication:
    def __init__(self, user_manager):
        self.user_manager = user_manager
        self.sessions = []  # This could be a list or another form of storage for session data

    def verify_login(self, email, password):
        user = self.user_manager.find_user_by_email(email)
        if user and user.check_password(password):
            print("Login successful")
            return user
        return None
    
    def record_session(self, user_id, login_time, logout_time):
        session = {
            'login_time': login_time,
            'logout_time': logout_time,
            'user_id': user_id
        }
        self.sessions.append(session)
        print("Session recorded")
