from type_of_person.person import Person


class Student(Person):
    def __init__(self, firstName, lastName, studentNum):
        self.firstName = firstName
        self.lastName = lastName
        self.studentNum = studentNum
    def getStudentNumber(self):
        return self.studentNum

    def setStudentNumber(self, studentNum):
        self.studentNum = studentNum
