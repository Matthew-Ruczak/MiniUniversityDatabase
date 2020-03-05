from type_of_person.employee import Employee
from type_of_person.student import Student


typesOfPersons = ("Employee", "Student")
listOfPersons = []


def addToDatabaseMenu():
    print("""
    What type of person would you like to add? (enter a number)
    1. Employee
    2. Student
    3. Exit
    """)
    userInput = input('\t')

    # Processing user's input
    if userInput == "1":
        addPersonToDatabase(typesOfPersons[0])
    elif userInput == "2":
        addPersonToDatabase(typesOfPersons[1])
    elif (userInput == "3"):
        mainMenu()
    else:
        print("Option not available, please try again")
        addToDatabaseMenu()
    mainMenu()


def addPersonToDatabase(personType):
    personFirstName = input('\tWhat is their first name? ')
    personLastName = input('\tWhat is their last name? ')
    if (personType == "Employee"):
        personSpecialNum = input('What is their unique employee number?')
        listOfPersons.append(Employee(personFirstName, personLastName, personSpecialNum))
        print(f"Successfully Added {personLastName}")
    else:
        personSpecialNum = input('What is their unique student number?')
        listOfPersons.append(Student(personFirstName, personLastName, personSpecialNum))
        print(f"Successfully Added {personLastName}")
    mainMenu()


def removePersonMenu():
    # Processing User input
    wasPersonRemoved = False
    personToRemoveSpecialNum = input("What is their employee number? (OR enter 0000 to exit")
    if personToRemoveSpecialNum == "0000":
        mainMenu()
    for person in listOfPersons:
        if person.getEmployeeNum() == personToRemoveSpecialNum:
            listOfPersons.remove(person)
            wasPersonRemoved = True
    if wasPersonRemoved:
        print("Employee was removed")
    else:
        print("Employee not found, please try again.")
        removePersonMenu()
    mainMenu()


def updatePersonMenu():
    personToUpdateSpecialNum = input("\tPlease enter unique number of the person you would like to update? (OR enter 0000 to exit)")
    if personToUpdateSpecialNum == "0000":
        mainMenu()
    personToUpdateObj = findPersonByNumber(personToUpdateSpecialNum)
    if personToUpdateObj == -1:
        print(f"Unique Number {personToUpdateSpecialNum} was not found, please try again.")
        updatePersonMenu()
    else:
        personToUpdateMenu(personToUpdateObj)


def personToUpdateMenu(personToUpdateObj):
    print(f"What would you like to update for {personToUpdateObj[0].getFullName()}?")
    print("""1. First Name
             2. Last Name
             3. Unique Number
             4. Exit
    """)
    userSelectedFieldToUpdate = input()

    if userSelectedFieldToUpdate == "1":
        newPersonFirstName = input("Please enter their new first name: ")
        personToUpdateObj[0].setFirstName(newPersonFirstName)
    elif userSelectedFieldToUpdate == "2":
        newPersonLastName = input("Please enter their new first name: ")
        personToUpdateObj[0].setLastName(newPersonLastName)
    elif userSelectedFieldToUpdate == "3":
        if personToUpdateObj[1] == Employee:
            newEmployeeNumber = input("What is their new Employee #")
            personToUpdateObj[0].setEmployeeNum(newEmployeeNumber)
        elif personToUpdateObj[1] == Student:
            newStudentNumber = input("What is their new Student #")
            personToUpdateObj[0].setStudentNumber(newStudentNumber)
    elif userSelectedFieldToUpdate == "4":
        mainMenu()
    else:
        print("Invalid input, please try again")
    personToUpdateMenu(personToUpdateObj)

def searchForPersonByIDMenu:
    searchForNum = input("What is their special number? (OR enter 0000 to exit)")
    searchResult = findPersonByNumber(searchForNum)
    if searchResult == -1:
        print(f'No person found with the special number {searchForNum}, please try again.')
    else:
        if type(searchResult[0]) == Employee:
            print(f"Employee {searchResult[0].getFullName()} {searchResult[0].getEmployeeNum()}")
        elif type(searchResult[0]) == Student:
            print(f"Student {searchResult[0].getFullName()} {searchResult[0].setStudentNumber()}")
        else:
            print(f"Error when searching for {searchForNum}, please try again")
    searchForPersonByIDMenu()

def displayAllEmployeesAndStudent():
    print("\t_______________________")
    print("\t\tPersons")
    print("\t-----------------------")
    for person in listOfPersons:
        if type(person) == Employee:
            print(f"\tEmployee {person.getFullName()} {person.getEmployeeNum()}")
        elif type(person) == Student:
            print(f"\tStudent {person.getFullName()} {person.getStudentNumber()}")
        else:
            print(f"Error with Person, data was not retrieved.")
    print("\t_______________________")
    mainMenu()


def mainMenu():
    print("""
    Welcome to Mini University Database
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    What would you like to do? (enter a number)
    1. Add
    2. Delete
    3. Update
    4. Search
    5. View All
    6. Exit
    ---------------------------------------""")
    userInput = input('\t')

    #Processing user's input
    if userInput == "1":
        addToDatabaseMenu()
    elif userInput == "2":
        removePersonMenu()
    elif userInput == "3":
        updatePersonMenu()
    elif userInput == "4":
        searchForPersonByIDMenu()
    elif userInput == "5":
        displayAllEmployeesAndStudent()
    elif userInput == "6":
        print("Please close the program using the exit button in the window")
    else:
        print("Invalid input, please enter a number from the above list. (Without a period)")
    mainMenu()

def findPersonByNumber(unqiueNum):
    for person in listOfPersons:
        if type(person) == Employee:
            if person.getEmployeeNum() == unqiueNum:
                return person, Employee
        if type(person) == Student:
            if person.getStudentNumber() == unqiueNum:
                return person, Student
    return -1   # No person was found

# Displaying the main menu when the user first enters the program
mainMenu()
