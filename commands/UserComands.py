from commands.Command import Command

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

class UpdateUserProfileCommand(Command):
    def __init__(self, kms, user_id, new_name, new_email, new_password):
        self.kms = kms
        self.user_id = user_id
        self.new_name = new_name
        self.new_email = new_email
        self.new_password = new_password

    def execute(self):
        self.kms.update_user_profile(self.user_id, name=self.new_name, email=self.new_email, password=self.new_password)
