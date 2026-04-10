from models.student import Student

class StudentService:
    def __init__(self, data):
        self.students = [Student.from_dict(s) for s in data.get("students", [])]

    def add_student(self, student_id, name):
        if any(s.student_id == student_id for s in self.students):
            print("❗ Student ID already exists")
            return
        self.students.append(Student(student_id, name))
        print("✅ Student added successfully")

    def view_students(self):
        if not self.students:
            print("No students found")
            return
        for s in self.students:
            print(s)

    def delete_student(self, student_id):
        self.students = [s for s in self.students if s.student_id != student_id]
        print("✅ Student deleted (if existed)")

    def exists(self, student_id):
        return any(s.student_id == student_id for s in self.students)

    def get_all(self):
        return [s.to_dict() for s in self.students]