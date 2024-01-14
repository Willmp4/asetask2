
from User import User

class Employee(User):
    
    def __init__(self, employee_id, name, role, email, password, biography, skills, experience):
        super().__init__(employee_id, name, role, email, password)
        self.employee_id = employee_id
        self.biography = biography
        self.skills = skills
        self.experience = experience

    @staticmethod
    def create_user(employee_id, name, role, email, password, biography, skills, experience):
        return Employee(employee_id, name, role, email, password, biography, skills, experience)


    def update_biography(self, biography):
        self.biography = biography
        print("Employee biography updated")

    def search_project(self, project_id):
        # This would interface with a project management component
        print("Searching for project")
        return "Project details for project_id: {}".format(project_id)

class Client(User):

    def __init__(self, client_id, name, email, password, company_name, role="client"):
        super().__init__(client_id, name, role, email, password)
        self.client_id = client_id
        self.company_name = company_name


    @staticmethod
    def create_user( client_id, name, email, password, company_name, ):
        return Client( client_id, name, email, password, company_name)

    def view_employee_biography(self, employee):
        print(f"Viewing biography for {employee.name}")



