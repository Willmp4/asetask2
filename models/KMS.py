class KnowledgeManagementSystem:
    def __init__(self, system_id, name, database):
        self.system_id = system_id
        self.name = name
        self.database = database

    def authenticate_user(self, email, password):
            # Combine clients and employees into one iterable
            all_users = self.database['clients'] + self.database['employees']

            # Use dot notation to access attributes of objects
            user = next((u for u in all_users if u.email == email and u.password == password), None)
            if user:
                print("Authentication successful")
                return user
            else:
                print("Authentication failed")
                return None
            
    def update_user_profile(self, user_id, name=None, email=None, password=None):
        user = next((u for u in self.database['clients'] + self.database['employees'] if u['user_id'] == user_id), None)
        if user:
            if name:
                user['name'] = name
            if email:
                user['email'] = email
            if password:
                user['password'] = password
            print("Profile updated")
        else:
            print("User not found")

    def provide_access(self, user):
        if user.role == "Client":
            print("Client access granted")
        elif user.role == "Employee":
            print("Employee access granted")
        else:
            print("Access denied")

    def generate_reports(self):
        pass

    def search_employees(self, criteria):
        matching_employees = []
        for employee in self.database['employees']:
            if all(criteria[key] == getattr(employee, key, None) for key in criteria):
                matching_employees.append(employee)
        return matching_employees

    def update_employee_biography(self, employee_id, biography_data):
        for employee in self.database['employees']:
            if employee.employee_id == employee_id:
                employee.biography.update_biography_info(**biography_data)
                print("Biography updated")
                return
        print("Employee not found")

    def add_document_to_biography(self, biography_id, document):
        for biography in self.database['biographies']:
            if biography.biography_id == biography_id:
                biography.add_document(document)
                print("Document added to biography")
                return
        print("Biography not found")
