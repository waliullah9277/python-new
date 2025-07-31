# Student List Manager Program
def add_student(students, name, roll, class_name):  # Function to add a student
    students.append({"name": name, "roll": roll, "class": class_name})  # Append student info to the list
    print(f"{name} added successfully")  # Confirmation message for adding student

def view_students(students):  # Function to view all students
    if not students:  # Check if the list is empty
        print("No students found")  # Message if no students are found
    else:
        for student in students:  # Loop through each student
            print(f"Name: {student['name']}, Roll: {student['roll']}, Class: {student['class']}")  # Print student details

def delete_student(students, roll):  # Function to delete a student by roll
    for i in range(len(students)):  # Loop through the list indices
        if students[i]["roll"] == roll:  # Check if roll matches
            removed = students.pop(i)  # Remove student from the list
            print(f"{removed['name']} deleted successfully")  # Confirmation message for deletion
            return  # Exit function after deletion
    print("Roll number not found")  # Error message if roll not found

def main():  # Main function to run the program
    students = []  # Initialize empty list for students
    while True:  # Infinite loop for menu
        print("\n1. Add Student")  # Menu option 1: Add student
        print("2. View List")  # Menu option 2: View list
        print("3. Delete Student")  # Menu option 3: Delete student
        print("4. Exit")  # Menu option 4: Exit
        choice = input("Choice: ")  # Get user's choice

        if choice == '1':  # Option to add a student
            name = input("Name: ")  # Input student name
            roll = int(input("Roll: "))  # Input roll number
            class_name = input("Class: ")  # Input class
            add_student(students, name, roll, class_name)  # Call function to add student
        elif choice == '2':  # Option to view students
            view_students(students)  # Call function to view students
        elif choice == '3':  # Option to delete a student
            roll = int(input("Roll number to delete: "))  # Input roll number to delete
            delete_student(students, roll)  # Call function to delete student
        elif choice == '4':  # Option to exit
            print("Program ended")  # Exit message
            break  # Break the loop to end program
        else:
            print("Invalid choice")  # Error message for invalid choice

main()  # Start the program