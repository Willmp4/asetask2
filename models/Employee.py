
from models.User import User
from biography.Biography import Biography
import uuid

#This is the Employee class that inherits from the User class
#Has a one to one relationship with the Biography class
class Employee(User):
    def __init__(self, user_id, name, role, email, password, biography_description, skills, experience, biography=None):
        #Super is used to inherit the attributes from the User class
        super().__init__(user_id, name, role, email, password)
        if biography is None:
            self.biography = Biography(str(uuid.uuid4()), biography_description, user_id, None, None)
        else:
            self.biography = biography
        self.skills = skills
        self.experience = experience
        self.set_password(password)
    
    #This method is used to convert the attributes of the class to a dictionary
    def to_dict(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'role': self.role,
            'email': self.email,
            'password': self.password,
            'biography': self.biography.to_dict(),
            'skills': self.skills,
            'experience': self.experience
        }

    #This method is used to create a new user
    #A static method is a method that knows nothing about the class or instance it was called on.
    @staticmethod
    def create_user(user_id, name, role, email, password, biography_description, skills, experience):
        return Employee(user_id, name, role, email, password, biography_description, skills, experience)

#This is the Client class that inherits from the User class
class Client(User):

    def __init__(self, user_id, name, email, password, company_name, role="client"):
        super().__init__(user_id, name, role, email, password)
        self.company_name = company_name
        self.set_password(password)

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'role': self.role,
            'email': self.email,
            'password': self.password,
            'company_name': self.company_name
        }


    @staticmethod
    def create_user( user_id, name, email, password, company_name, ):
        return Client( user_id, name, email, password, company_name)


