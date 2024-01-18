from models.Employee import Employee

class AdminActions:
    def __init__(self, user_manager, user, kms):
        self.user_manager = user_manager
        self.user = user
        self.kms = kms

    def access_all_biographies(self):
        employees = [u for u in self.user_manager.users.values() if isinstance(u, Employee)]
        return [(employee.name, employee.biography.to_dict()) for employee in employees]
      
    def list_documents_for_employee(self, employee_name):
        employee = next((emp for emp in self.user_manager.users.values() if isinstance(emp, Employee) and emp.name == employee_name), None)
        if employee:
            return [(doc.title, doc.document_id) for doc in employee.biography.documents]
        else:
            print("Employee with the given name not found")
            return []

    def edit_any_document_by_title(self, employee_name, doc_title, new_title, new_content):
        employee = next((emp for emp in self.user_manager.users.values() if isinstance(emp, Employee) and emp.name == employee_name), None)
        if employee:
            document = next((doc for doc in employee.biography.documents if doc.title == doc_title), None)
            if document:
                self.kms.update_document_in_biography(employee.biography.biography_id, document.title, new_title, new_content)
            else:
                print("Document with the given title not found")
        else:
            print("Employee with the given name not found")