from type_of_person.person import Person


class Employee(Person):
    def __init__(self,firstName, lastName, employeeNum):
        self.firstName = firstName
        self.lastName = lastName
        self.employeeNum = employeeNum
    def getEmployeeNum(self):
        return self.employeeNum

    def setEmployeeNum(self, employeeNum):
        self.employeeNum = employeeNum
