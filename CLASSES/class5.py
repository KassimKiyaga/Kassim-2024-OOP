class Student:
    def __init__(self, name, student_id, grades=None):
        self.name = name
        self.student_id = student_id
        self.grades = grades if grades is not None else []

    def get_average(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        else:
            return "No grades available"
