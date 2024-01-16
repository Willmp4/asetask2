from Command import Command

class CreateUserCommand(Command):
    def __init__(self, kms, user_type, **additional_params):
        self.kms = kms
        self.user_type = user_type
        self.additional_params = additional_params

    def execute(self):
        self.kms.create_user(self.user_type, **self.additional_params)


class LoginUserCommand(Command):
    def __init__(self, authenticator, email, password):
        self.authenticator = authenticator
        self.email = email
        self.password = password

    def execute(self):
        user = self.authenticator.verify_login(self.email, self.password)
        return user  # Return the user object if login is successful
