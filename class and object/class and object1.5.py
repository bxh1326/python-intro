class Student:
    domain = 'icloud.com'
    def __init__(self, first, last, email, grade):
        self.first = first
        self.last = last
        self.email = email
        self.grade = grade
    def getEmail(self):
        email = self.first + '.' + self.last + '@' + self.domain
        return email
    def compareGrade(self, anotherStudent):
        if self.grade > anotherStudent.grade:
            print(self.first, 'grade is greater than', anotherStudent.first, 'grade')
        elif self.grade < anotherStudent.grade:
            print(self.first, 'grade is less than', anotherStudent.first, 'grade')
        elif self.grade == anotherStudent.grade:
            print(self.first, 'grade is the same as', anotherStudent.first, 'grade')
student1 = Student('bridget','he','bridget100101@icloud.com', '95')
student2 = Student('madison','marino','madisonrmarino@me.com', '95')
student3 = Student('madelyn','zambrano','zambmad@icloud.com', '90')
student2.domain = 'me.com'
print(student1.getEmail())
print(student2.getEmail())
print(student3.getEmail())
student1.compareGrade(student2)
