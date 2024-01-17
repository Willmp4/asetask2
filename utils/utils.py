def read_documents(employees):
    for emp in employees:
        print(f"{emp.name} - {emp.biography.description}")

    employee_name = input("Which employee's biography do you want to read?: ").lower()
    employee = next((emp for emp in employees if emp.name.lower() == employee_name), None)

    if not employee: 
        print("Employee not found")
        return
    
    print(f"Biography for {employee.name}: {employee.biography.description}")
    for doc in employee.biography.documents:
        print(f"Document: {doc.title}")

    doc_choice = input("Which document do you want to read?: ").lower()
    document = next((doc for doc in employee.biography.documents if doc.title.lower() == doc_choice), None)

    if document:
        print(f"Title: {document.title}\n{document.content}")
    else:
        print("Document not found")
