def add_student():
    print("___________________________")
    print(" Add Student Information")
    print("---------------------------")

    # Prompt user for student information
    first_name = input("Enter First Name: ")
    middle_initial = input("Enter Middle Initial: ")
    last_name = input("Enter Last Name: ")

    while True:
        student_id = input("Enter Student ID Number: ")
        with open('student_information.txt', 'r') as file:
            for line in file:
                existing_studentID = line.strip().split(',')
                if existing_studentID[0] == student_id:
                    print("Student ID already exists. Please enter a different Student ID.")
                    break
            else:
                break

    year_level = input("Enter Year Level: ")
    course_code = input("Enter Course Code: ")

    with open('courses.txt', 'r+') as course_file:
        courses = course_file.readlines()

        # Check if course_code already exists
        course_exists = False
        for line in courses:
            course_index = line.strip().split(',')

            if course_index[0] == course_code:
                course_exists = True
                break

        if course_exists:
            # Write student information to file
            with open('student_information.txt', 'a') as file:
                file.write(f"{student_id},{course_code},{year_level},{first_name},{middle_initial},{last_name}\n")

        else:
            new_course = input("Do you want to add this new course code? (Yes or No): ")
            if new_course.lower() == "yes":
                new_courseName = input("Enter New Course Name: ")
                course_file.write(f"{course_code},{new_courseName}\n")

            # Write student information to file
            with open('student_information.txt', 'a') as file:
                file.write(f"{student_id},{course_code},{year_level},{first_name},{middle_initial},{last_name}\n")

    print("Student Added Successfully!")
    input("Press Enter to Continue")


def search_student():
    print("_____________________________")
    print(" Search Student Information")
    print("-----------------------------")

    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    student_id = input("Enter Student ID Number: ")

    file = open('student_information.txt', 'r')

    student_found = False

    for line in file:
        student = line.strip().split(',')
        if (
                student[0].lower() == student_id.lower()
                and student[3].lower() == first_name.lower()
                and student[5].lower() == last_name.lower()
        ):
            print("_________________")
            print(" STUDENT FOUND!")
            print("-----------------")

            print(f"Student Name: {student[3]} {student[4]} {student[5]}")
            print(f"Student ID Number: {student[0]}")
            print(f"Course Code: {student[1]} and Year Level: {student[2]}")

            student_found = True
            break

    if not student_found:
        print(
            f"No Student Found with First Name '{first_name}', Last Name '{last_name}' and ID Number '{student_id}'"
        )

    file.close()

    input("Press Enter to Continue")


def update_student():
    print("____________________________")
    print(" Update Student Information")
    print("----------------------------")

    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    student_id = input("Enter Student ID Number: ")

    with open('student_information.txt', 'r') as file:
        students = file.readlines()

    student_found = False
    updated_students = []

    for line in students:
        student = line.strip().split(',')

        if (
                student[0].lower() == student_id.lower()
                and student[3].lower() == first_name.lower()
                and student[5].lower() == last_name.lower()
        ):
            student_found = True
            print("________________________________")
            print(" Enter Student New Information ")
            print("--------------------------------")

            student[3] = input("Enter First Name: ")
            student[4] = input("Enter Middle Initial: ")
            student[5] = input("Enter Last Name: ")

            while True:
                student[0] = input("Enter New Student ID No: ")

                with open('student_information.txt', 'r') as file:
                    for line in file:
                        existing_studentID = line.strip().split(',')
                        if existing_studentID[0] == student[0]:
                            print("Student ID already exists. Please enter a different Student ID.")
                            break
                    else:
                        break

            student[2] = input("Enter Year Level: ")
            student[1] = input("Enter Course Code: ")

            with open('courses.txt', 'r') as file:
                courses = file.readlines()

            course_exists = False
            for line in courses:
                course_index = line.strip().split(',')
                if course_index[0].lower() == student[1].lower():
                    course_exists = True
                    break

            if not course_exists:
                new_course = input("Do you want to add this new course code? (Yes or No): ")
                if new_course.lower() == "yes":
                    new_courseCode = input("Enter New Course Code: ")
                    new_courseName = input("Enter New Course Name: ")
                    with open('courses.txt', 'a') as file:  # Open file in append mode ('a')
                        file.write(f"{new_courseCode},{new_courseName}\n")

        updated_students.append(','.join(student))

    if not student_found:
        print(f"No Student Found with First Name '{first_name}', Last Name '{last_name}', and ID Number '{student_id}'")
    else:
        with open('student_information.txt', 'w') as file:
            file.write('\n'.join(updated_students))  # Write the updated students with newlines between each entry

    print("Student information updated successfully!")
    input("Press any key to continue")


def delete_student():
    print("___________________________")
    print(" Delete Student Information")
    print("---------------------------")

    student_id = input("Enter Student ID Number to delete: ")

    found = False
    # Read student information from file
    with open('student_information.txt', 'r') as file:
        studentList = file.readlines()

    # Search for the student ID in the file
    with open('student_information.txt', 'w') as file:
        for line in studentList:
            if line.startswith(student_id + ','):
                found = True
                continue  # Skip writing this line to the file
            file.write(line)

    if found:
        print("Student Deleted Successfully!")
    else:
        print("Student ID not found.")

    input("Press Enter to Continue")


def list_ofStudents():
    print("___________________________")
    print("    View All Students      ")
    print("---------------------------")

    with open('student_information.txt', 'r') as file:
        student_list = file.readlines()

    if len(student_list) == 0:
        print("No student records found.")
    else:
        print("Student ID\tCourse\tYear Level\tFirst Name\tMiddle Initial\tLast Name")
        print("---------------------------------------------------------------------")
        for line in student_list:
            index = line.strip().split(',')

            if len(index) >= 6:  # Check if line has enough elements
                student_id = index[0]
                course_code = index[1]
                year_level = index[2]
                first_name = index[3]
                middle_initial = index[4]
                last_name = index[5]

                print(f"{student_id}\t\t{course_code}\t\t{year_level}\t\t{first_name}\t\t\t{middle_initial}\t\t\t{last_name}")
            else:
                print("Invalid student record:", line.rstrip())

    input("Press Enter to Continue")


