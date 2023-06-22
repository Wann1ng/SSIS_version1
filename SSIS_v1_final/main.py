import student_information
import courses


# Print out menu options
def student_info():
    print("1. Add Student Information")
    print("2. Search Student Information")
    print("3. Update Student Information")
    print("4. Delete Student Information")
    print("5. List of Students")
    print("6. Exit")


def student_course():
    print("1. Add Course")
    print("2. Search Course")
    print("3. Update Course")
    print("4. Delete Course")
    print("5. List of Courses")
    print("6. Exit")


while True:
    print("1. CRUDL for Student Information")
    print("2. CRUDL for Courses")
    print("3. Exit")

    option = input("Enter your choice: ")

    if option == '1':
        while True:
            student_info()

            option1 = input("Enter your choice: ")

            if option1 == '1':
                student_information.add_student()
            elif option1 == '2':
                student_information.search_student()
            elif option1 == '3':
                student_information.update_student()
            elif option1 == '4':
                student_information.delete_student()
            elif option1 == '5':
                student_information.list_ofStudents()
            elif option1 == '6':
                break
            else:
                print("Invalid choice. Please try again.")

    elif option == '2':
        while True:
            student_course()

            option2 = input("Enter your choice: ")

            if option2 == '1':
                courses.add_course()
            elif option2 == '2':
                courses.search_course()
            elif option2 == '3':
                courses.update_course()
            elif option2 == '4':
                courses.delete_course()
            elif option2 == '5':
                courses.list_ofCourses()
            elif option2 == '6':
                break
            else:
                print("Invalid choice. Please try again.")

    elif option == '3':
        print("Thank You For Using This System!")
        break

    else:
        print("Invalid choice. Please try again.")
        