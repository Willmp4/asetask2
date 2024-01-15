
from User import User
from Biography import Biography
import uuid

class Employee(User):
    def __init__(self, user_id, name, role, email, password, biography_description, skills, experience, biography=None):
        super().__init__(user_id, name, role, email, password)
        if biography is None:
            self.biography = Biography(str(uuid.uuid4()), name, biography_description, user_id, None, None)
        else:
            self.biography = biography
        self.skills = skills
        self.experience = experience
    
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

    @staticmethod
    def create_user(user_id, name, role, email, password, biography_description, skills, experience):
        return Employee(user_id, name, role, email, password, biography_description, skills, experience)


class Client(User):

    def __init__(self, user_id, name, email, password, company_name, role="client"):
        super().__init__(user_id, name, role, email, password)
        self.company_name = company_name

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


