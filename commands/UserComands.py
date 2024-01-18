from commands.Command import Command
#The commands are using actions by calling the methods of the actions.
#This is create user command

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
    def __init__(self, actions, **kwargs):
        self.actions = actions
        self.kwargs = kwargs

    def execute(self):
        self.actions.edit_account(**self.kwargs)
