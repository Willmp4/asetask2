#Q: explain the purpose of this class and how it relates to biographies
#This class is used to create a document object that can be uploaded to the database. 
#It contains the document's title, content, biography, and upload date.
#It has a many to one relationship with the biography class.
class Document:
    def __init__(self, document_id, title, content, biography, upload_date):
        self.document_id = document_id
        self.title = title
        self.content = content
        self.biography = biography
        self.upload_date = upload_date

    def to_dict(self):
        return {
            'document_id': self.document_id,
            'title': self.title,
            'content': self.content,
            'biography': self.biography,
            'upload_date': self.upload_date
        }
