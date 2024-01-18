from commands.UserComands import CreateUserCommand, LoginUserCommand, UpdateUserProfileCommand
from commands.BiographyComands import AddDocumentToBiographyCommand, ReadBiographyCommand, UpdateBiographyCommand, UpdateDocumentCommand, GetEmployeeDocumentsCommand, AccessAllBiographiesCommand, ListDocumentsForEmployeeCommand, EditAnyDocumentByTitleCommand

class CommandIssuer:
    def __init__(self, invoker, user_manager, kms):
        self.invoker = invoker
        self.user_manager = user_manager
        self.kms = kms

    def issue_command(self, command_type, **kwargs):
        command = None

        if command_type == 'add_document':
            actions = kwargs['actions']
            command = AddDocumentToBiographyCommand(actions, kwargs['title'], kwargs['content'])

        elif command_type == 'edit_user':
            actions = kwargs['actions']
            command = UpdateUserProfileCommand(actions, name=kwargs['name'], email=kwargs['email'], password=kwargs['password'])

        elif command_type == 'view_documents':
            actions = kwargs['actions']
            command = ReadBiographyCommand(actions)

        elif command_type == 'edit_biography':
            actions = kwargs['actions']
            command = UpdateBiographyCommand(actions, kwargs['new_description'])

        elif command_type == 'edit_document':
            actions = kwargs['actions']
            command = UpdateDocumentCommand(actions, kwargs['doc_id'], kwargs['new_title'], kwargs['new_content'])

        elif command_type == 'create_user':
            command = CreateUserCommand(self.kms, **kwargs)

        elif command_type == 'login_user':
            authenticator = kwargs['authenticator']
            command = LoginUserCommand(authenticator, kwargs['email'], kwargs['password'])
            
        elif command_type == 'get_document':
            actions = kwargs['actions']
            command = GetEmployeeDocumentsCommand(actions)
        
        elif command_type == 'access_all_biographies':
            actions = kwargs['actions']
            command = AccessAllBiographiesCommand(actions)

        elif command_type == 'list_documents_for_employee':
            actions = kwargs['actions']
            command = ListDocumentsForEmployeeCommand(actions, kwargs['employee_name'])

        elif command_type == 'edit_any_document_by_title':
            actions = kwargs['actions']
            command = EditAnyDocumentByTitleCommand(actions, kwargs['employee_name'], kwargs['doc_title'], kwargs['new_title'], kwargs['new_content'])

        if command:
            return self.invoker.store_and_execute(command)  
        else:
            print("Invalid command type")
