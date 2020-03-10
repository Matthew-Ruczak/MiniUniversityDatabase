from type_of_person.employee import Employee
from type_of_person.student import Student


listOfPersons = []


def add_person_menu():
    print("""
    What type of person would you like to add? (enter a number)
    1. Employee
    2. Student
    3. Exit
    """)
    user_input = input('\t')

    # Processing user's input
    if user_input == "1":
        person_info_to_add_menu(Employee)
    elif user_input == "2":
        person_info_to_add_menu(Student)
    elif user_input == "3":
        main_menu()
    else:
        print("\tOption not available, please try again")
        add_person_menu()
    main_menu()


def person_info_to_add_menu(person_type):
    person_first_name = input('\tWhat is their first name? ')
    person_last_name = input('\tWhat is their last name? ')
    newly_created_person = ""
    if person_type == Employee:  # Creating an Employee
        person_special_num = input('\tWhat is their unique employee number?')
        newly_created_person = Employee(person_first_name, person_last_name, person_special_num)
    else:   # Creating a Student
        person_special_num = input('\tWhat is their unique student number?')
        newly_created_person = Student(person_first_name, person_last_name, person_special_num)
    listOfPersons.append(newly_created_person)
    print(f"\tSuccessfully Added {person_first_name} {person_last_name}")
    main_menu()


def remove_person_menu():
    # Checking if there are people to delete
    if len(listOfPersons) <= 0:
        print('\tDatabase is empty, no person to remove.')
        main_menu()
    # Processing User input
    person_to_remove_special_num = input("\tWhat is the person's special number? (OR enter 0000 to exit) ")
    if person_to_remove_special_num == "0000":
        main_menu()
    # searching for person to remove
    search_result = find_person_by_special_num(person_to_remove_special_num)
    if search_result != -1:     # If a person was found
        listOfPersons.remove(search_result)
        print(f"\tPerson {person_to_remove_special_num} was removed")
    else:   # Since a person was not found
        print("\tEmployee not found, please try again.")
        remove_person_menu()     # Letting user try again
    main_menu()


def update_person_menu():
    # Checking if there are people to update
    if len(listOfPersons) <= 0:
        print('\tDatabase is empty, no person to update.')
        main_menu()

    print('\tUpdate Person Menu')
    person_to_update_special_num = input("\tPlease enter their unique number or enter 0000 to exit: ")
    if person_to_update_special_num == "0000":
        main_menu()
    person_to_update_obj = find_person_by_special_num(person_to_update_special_num)
    if person_to_update_obj == -1:
        print(f"\tUnique Number {person_to_update_special_num} was not found, please try again.")
        update_person_menu()
    else:
        person_to_update_menu(person_to_update_obj)


def person_to_update_menu(person_to_update_obj):
    print(f"\tWhat would you like to update for {person_to_update_obj.getFullName()}?")
    print("""
         1. First Name
         2. Last Name
         3. Unique Number
         4. Exit
    """)
    field_to_update = input()

    if field_to_update == "1":
        new_person_first_name = input("\tPlease enter their new first name: ")
        person_to_update_obj.setFirstName(new_person_first_name)
    elif field_to_update == "2":
        new_person_last_name = input("\tPlease enter their new first name: ")
        person_to_update_obj.setLastName(new_person_last_name)
    elif field_to_update == "3":
        # Updating Person's special number (depending on what type of Person they are)
        if type(person_to_update_obj) == Employee:
            person_to_update_obj.setEmployeeNum(input("\tWhat is their new Employee #"))
        elif type(person_to_update_obj) == Student:
            person_to_update_obj.setStudentNumber(input("\tWhat is their new Student #"))
    elif field_to_update == "4":
        main_menu()
    else:
        print("\tInvalid input, please try again")
    person_to_update_menu(person_to_update_obj)  # Let's the user update another field or try again


def search_for_person_by_id_menu():
    # Checking if there are people to delete
    if len(listOfPersons) <= 0:
        print('\tDatabase is empty, no person to search for.')
        main_menu()

    search_for_special_num = input("\tWhat is their special number? (OR enter 0000 to exit) ")
    if search_for_special_num == "0000":
        main_menu()
    search_result = find_person_by_special_num(search_for_special_num)
    if search_result == -1:
        print(f'\tNo person found with the special number {search_for_special_num}, please try again.')
    else:
        if type(search_result) == Employee:
            print(f"\tEmployee {search_result.getFullName()} {search_result.getEmployeeNum()}")
        elif type(search_result[0]) == Student:
            print(f"\tStudent {search_result.getFullName()} {search_result.getStudentNumber()}")
        else:
            print(f"\tError when searching for {search_for_special_num}, please try again")
    search_for_person_by_id_menu()


def display_all_persons():
    print("\t_______________________")
    print("\t\tPersons")
    print("\t-----------------------")
    # Checking if there are people to display
    if len(listOfPersons) <= 0:
        print('\tEmpty')
    else:
        for person in listOfPersons:
            if type(person) == Employee:
                print(f"\tEmployee {person.getFullName()} {person.getEmployeeNum()}")
            elif type(person) == Student:
                print(f"\tStudent {person.getFullName()} {person.getStudentNumber()}")
            else:
                print(f"\tError with Person, data was not retrieved.")
    print("\t_______________________")
    main_menu()


def main_menu():
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
    selected_option = input('\t')

    # Processing user's input
    if selected_option == "1":
        add_person_menu()
    elif selected_option == "2":
        remove_person_menu()
    elif selected_option == "3":
        update_person_menu()
    elif selected_option == "4":
        search_for_person_by_id_menu()
    elif selected_option == "5":
        display_all_persons()
    elif selected_option == "6":
        exit(0)
    else:
        print("\tInvalid input, please enter a number from the above list. (Without a period)")
    main_menu()


def find_person_by_special_num(special_num):
    for person in listOfPersons:
        if type(person) == Employee:
            if person.getEmployeeNum() == special_num:
                return person
        if type(person) == Student:
            if person.getStudentNumber() == special_num:
                return person
    return -1   # No person was found


# Displaying the main menu when the user first enters the program
main_menu()
