class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def getFirstName(self):
        return self.firstName
    def getLastName(self):
        return self.lastName
    def getFullName(self):
        return self.firstName + " " + self.lastName

    def setFirstName(self, firstName):
        self.firstName = firstName
    def setLastName(self, lastName):
        self.lastName = lastName