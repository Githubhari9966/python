class Public:
    def __init__(self,name,email):
        self.name = name
        self.email = email
    def display(self):
        print("Name of the person: ", self.name)
        print("Email: ", self.email)
class Student(Public):
    StudentCount = 0
    def __init__(self,name,email,student_id):
        Public.__init__(self,name,email)
        self.student_id = student_id
        Student.StudentCount +=1
    def displayCount(self):
        print("Total Students:", Student.StudentCount)
    def display(self):
        print("Student Details:")
        Public.display(self)
        print("Student Id: ",self.student_id)
class Librarian(Public):
    StudentCount = 0
    def __init__(self,name,email,employee_id):
        super().__init__(name,email)
        self.employee_id = employee_id
    def display(self):
        print("Employee Details:")
        Public.display(self)
        print("Employee Id: ",self.employee_id)
class Book():
    def __init__(self, bname, author, book_id):
        self.book_name = bname
        self.author = author
        self.book_id = book_id
    def display(self):
        print("Book Details")
        print("Book_Name: ", self.book_name)
        print("Author: ", self.author)
        print("Book_ID: ", self.book_id)
class Borrow_Book(Student,Book):
    def __init__(self, name, email, student_id, bname, author, book_id):
        Student.__init__(self,name,email,student_id)
        Book.__init__(self, bname, author, book_id)
    def display(self):
        print("Borrowed Book Details:")
        Student.display(self)
        Book.display(self)
list1= []
list1.append(Student('name1', 'name1@gmail.com', 985))
list1.append(Student('name2', 'name2@gmail.com', 123))
list1.append(Librarian('guy1', 'guy1@gmail.com', 789))
list1.append(Librarian('guy2', 'guy2@gmail.com', 847))
list1.append(Book('ISL', 'Robert Tibshirani', 1012368))
list1.append(Book('Java essentials', 'kutner', 87605))
list1.append(Borrow_Book('name1', 'name1@gmail.com', 985, 'ISL', 'Robert Tibshirani', 1012368))
for obj, item in enumerate(list1):
    item.display()
    print("\n")
    if obj == len(list1)-1:
        item.displayCount()