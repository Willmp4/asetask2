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

class AccessAllBiographiesCommand(Command):
    def __init__(self, actions):
        self.actions = actions

    def execute(self):
        return self.actions.access_all_biographies()

class ListDocumentsForEmployeeCommand(Command):
    def __init__(self, actions, employee_name):
        self.actions = actions
        self.employee_name = employee_name

    def execute(self):
        return self.actions.list_documents_for_employee(self.employee_name)

class EditAnyDocumentByTitleCommand(Command):
    def __init__(self, actions, employee_name, doc_title, new_title, new_content):
        self.actions = actions
        self.employee_name = employee_name
        self.doc_title = doc_title
        self.new_title = new_title
        self.new_content = new_content

    def execute(self):
        self.actions.edit_any_document_by_title(self.employee_name, self.doc_title, self.new_title, self.new_content)




