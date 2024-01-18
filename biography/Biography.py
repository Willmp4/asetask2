#This is the Biography class
#This class is used to define the attributes and methods of a biography
#The biography has a biography id, a description, an employee id, a start date, an end date and a list of documents
class Biography:
    def __init__(self, biography_id, description, employee_id, start_date, end_date):
        self.biography_id = biography_id
        self.description = description
        self.employee_id = employee_id
        self.start_date = start_date
        self.end_date = end_date
        self.documents = []
    #This method is used to convert the attributes of the class to a dictionary
    def to_dict(self):
        return {
            'biography_id': self.biography_id,
            'description': self.description,
            'employee_id': self.employee_id,
            'start_date': self.start_date,
            'end_date': self.end_date,
            # Convert documents to a list of dictionaries if necessary
            'documents': [doc.to_dict() for doc in self.documents]
        }

    #This method is used to add a document to the biography
    def add_document(self, document):
        self.documents.append(document)
        print("Document added")

    #This method is used to update the biography info
    def update_biography_info(self, name=None, description=None):
        if name:
            self.name = name
        if description:
            self.description = description
        print("Biography info updated")

    #This method is used to update the document info
    def search_document(self, document_id):
        document = next((d for d in self.documents if d.document_id == document_id), None)
        if document:
            print("Document found")
            return document
        print("Document not found")
        return None
