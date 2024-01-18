from commands.Command import Command
from document.Document import Document

#The commands are using actions by calling the methods of the actions. #
#For example, the AddDocumentToBiographyCommand class calls the add_document method of the EmployeeActions class.

#This is the AddDocumentToBiographyCommand class
#This class inherits from the Command class
class AddDocumentToBiographyCommand(Command):
    def __init__(self, actions, title, content):
        self.actions = actions
        self.title = title
        self.content = content

    def execute(self):
        self.actions.add_document(self.title, self.content)

# This is the GetEmployeeDocumentsCommand class

class GetEmployeeDocumentsCommand(Command):
    def __init__(self, actions):
        self.actions = actions

    def execute(self):
        return self.actions.get_user_documents()  # Return the documents

#This is the ReadBiographyCommand class
class ReadBiographyCommand(Command):
    def __init__(self, actions):
        self.actions = actions

    def execute(self):
        self.actions.read_documents()

#This is the UpdateBiographyCommand class
class UpdateBiographyCommand(Command):
    def __init__(self, actions, new_description):
        self.actions = actions
        self.new_description = new_description

    def execute(self):
        self.actions.edit_biography(self.new_description)

#This is the UpdateDocumentCommand class
class UpdateDocumentCommand(Command):
    def __init__(self, actions, document_id, new_title, new_content):
        self.actions = actions
        self.document_id = document_id
        self.new_title = new_title
        self.new_content = new_content

    def execute(self):
        self.actions.edit_document(self.document_id, self.new_title, self.new_content)

