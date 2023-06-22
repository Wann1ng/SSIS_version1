def add_course():
    print("___________________________")
    print(" Add Course Information")
    print("---------------------------")

    file = open('courses.txt', 'a')

    course_code = input("Enter Course Code: ")
    course_name = input("Enter Course Name: ")

    # Write student information to file
    file.write(f"{course_code},{course_name}\n")

    file.close()

    print("Course Added Successfully!")
    input("Press Enter to Continue")


def search_course():
    print("___________________________")
    print(" Search Course Information")
    print("---------------------------")

    course_code = input("Enter Course Code to search: ")

    found = False

    # Read the file and search for the course code
    with open('courses.txt', 'r') as file:
        for line in file:
            course_index = line.strip().split(',')
            if course_index[0].lower() == course_code.lower() :
                found = True
                print("Course Found!")
                print("Course Code:", course_index[0])
                print("Course Name:", course_index[1])
                break

    if not found:
        print("Course Not Found!")

    input("Press Enter to Continue")


def update_course():
    print("___________________________")
    print(" Update Course Information")
    print("---------------------------")

    course_code = input("Enter Course Code to update: ")

    found = False

    # Read the file and search for the course code
    with open('courses.txt', 'r') as file:
        course_file = file.readlines()

    # Check if the course code exists in the file
    with open('courses.txt', 'w') as file:
        for line in course_file:
            course_info = line.strip().split(',')
            if course_info[0] == course_code:
                found = True

                new_course_code = input("Enter new Course Code: ")
                new_course_name = input("Enter new Course Name: ")
                file.write(f"{new_course_code},{new_course_name}\n")
                print("Course Updated!")

                # Update student information file
                updated_student_lines = []
                with open('student_information.txt', 'r') as student_file:
                    student_lines = student_file.readlines()

                for line in student_lines:
                    student_info = line.strip().split(',')
                    if student_info[1] == course_code:
                        updated_line = f"{student_info[0]},{new_course_code},{student_info[2]},{student_info[3]},{student_info[4]},{student_info[5]}\n"
                        updated_student_lines.append(updated_line)
                    else:
                        updated_student_lines.append(line)

                with open('student_information.txt', 'w') as student_file:
                    for line in updated_student_lines:
                        student_file.write(line)

                break
            else:
                file.write(line)

    if not found:
        print("Course Code Not Found!")

    input("Press Enter to Continue")


def delete_course():
    print("___________________________")
    print(" Delete Course Information")
    print("---------------------------")

    course_code = input("Enter Course Code to delete: ")

    found = False

    # Read the file and search for the course code
    with open('courses.txt', 'r') as course_file:
        course_lines = course_file.readlines()

    # Check if the course code exists in the file
    with open('courses.txt', 'w') as course_file:
        for line in course_lines:
            course_index = line.strip().split(',')
            if course_index[0].lower() == course_code.lower():
                found = True
                print("Course Deleted!")
            else:
                course_file.write(line)

    if not found:
        print("Course Not Found!")

    # Delete student information if the course code exists
    if found:

        student_found = False
        # Read the student information file
        with open('student_information.txt', 'r') as student_file:
            student_lines = student_file.readlines()

        # Check if students exist under the course code
        updated_student_lines = []
        count = 0
        for line in student_lines:
            student_index = line.strip().split(',')
            if student_index[1].lower() == course_code.lower():
                student_found = True
                count = count + 1
                if count <= 1:
                    print("Students under the course code deleted!")
            else:
                updated_student_lines.append(line)
        if not student_found:
            print("No students found under this course.")

        # Write updated student information back to the file
        with open('student_information.txt', 'w') as student_file:
            for line in updated_student_lines:
                student_file.write(line)

    input("Press Enter to Continue")


def list_ofCourses():
    print("___________________________")
    print("       View Courses        ")
    print("---------------------------")

    with open('courses.txt', 'r') as file:
        courses = file.readlines()

    if len(courses) == 0:
        print("No course records found.")
    else:
        print("Course Code\t||Course Name")
        print("------------------------")
        for line in courses:
            index = line.strip().split(',')
            if len(index) >= 2:
                course_code = index[0]
                course_name = index[1]
                print(f"{course_code}\t\t{course_name}")

    input("Press Enter to Continue")


