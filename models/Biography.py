class Biography:
    def __init__(self, biography_id, name, description, client_id, start_date, end_date):
        self.biography_id = biography_id
        self.name = name
        self.description = description
        self.client_id = client_id
        self.start_date = start_date
        self.end_date = end_date
        self.documents = []

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
