class Biography:
    def __init__(self, biography_id, name, description, employee_id, start_date, end_date):
        self.biography_id = biography_id
        self.name = name
        self.description = description
        self.employee_id = employee_id
        self.start_date = start_date
        self.end_date = end_date
        self.documents = []

    def to_dict(self):
        return {
            'biography_id': self.biography_id,
            'name': self.name,
            'description': self.description,
            'employee_id': self.employee_id,
            'start_date': self.start_date,
            'end_date': self.end_date,
            # Convert documents to a list of dictionaries if necessary
            'documents': [doc.to_dict() for doc in self.documents]
        }

    def add_document(self, document):
        self.documents.append(document)
        print("Document added")

    def update_biography_info(self, name=None, description=None):
        if name:
            self.name = name
        if description:
            self.description = description
        print("Biography info updated")

    def search_document(self, document_id):
        document = next((d for d in self.documents if d.document_id == document_id), None)
        if document:
            print("Document found")
            return document
        print("Document not found")
        return None
