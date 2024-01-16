from Command import Command
from Document import Document
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
    