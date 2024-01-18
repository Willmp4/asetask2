from commands.Command import Command
from document.Document import Document

class AddDocumentToBiographyCommand(Command):
    def __init__(self, actions, title, content):
        self.actions = actions
        self.title = title
        self.content = content

    def execute(self):
        self.actions.add_document(self.title, self.content)

class GetEmployeeDocumentsCommand(Command):
    def __init__(self, actions):
        self.actions = actions

    def execute(self):
        return self.actions.get_user_documents()  # Return the documents


class ReadBiographyCommand(Command):
    def __init__(self, actions):
        self.actions = actions

    def execute(self):
        self.actions.read_documents()


class UpdateBiographyCommand(Command):
    def __init__(self, actions, new_description):
        self.actions = actions
        self.new_description = new_description

    def execute(self):
        self.actions.edit_biography(self.new_description)

class UpdateDocumentCommand(Command):
    def __init__(self, actions, document_id, new_title, new_content):
        self.actions = actions
        self.document_id = document_id
        self.new_title = new_title
        self.new_content = new_content

    def execute(self):
        self.actions.edit_document(self.document_id, self.new_title, self.new_content)

