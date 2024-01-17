from commands.Command import Command
from document.Document import Document
import uuid

class AddDocumentToBiographyCommand(Command):
    def __init__(self, kms, employee, title, content):
        self.kms = kms
        self.employee = employee
        self.title = title
        self.content = content

    def execute(self):
        document_id = str(uuid.uuid4())
        document = Document(document_id, self.title, self.content, self.employee.biography.biography_id, None)
        self.kms.add_document_to_biography(self.employee.biography.biography_id, document)


class ReadBiographyCommand(Command):
    def __init__(self, actions):
        self.actions = actions

    def execute(self):
        self.actions.read_documents()


class UpdateBiographyCommand(Command):
    def __init__(self, kms, biography_id, new_description):
        self.kms = kms
        self.biography_id = biography_id
        self.new_description = new_description

    def execute(self):
        self.kms.update_biography(self.biography_id, self.new_description)


class UpdateDocumentCommand(Command):
    def __init__(self, kms, biography_id, document_id, new_title, new_content):
        self.kms = kms
        self.biography_id = biography_id
        self.document_id = document_id
        self.new_title = new_title
        self.new_content = new_content

    def execute(self):
        self.kms.update_document_in_biography(self.biography_id, self.document_id, self.new_title, self.new_content)

    