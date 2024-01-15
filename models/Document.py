
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

    def upload(self, db):
        db['documents'].append(self)
        print("Document uploaded")

    def download(self):
        print(f"Document titled '{self.title}' downloaded.")

    def update(self, title=None, content=None):
        if title:
            self.title = title
        if content:
            self.content = content
        print("Document updated")
