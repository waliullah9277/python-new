# Student List Manager Program
# add student function here
def add_student(students, name, roll, class_name):
    for student in students:
        if student["roll"] == roll:
            print("Error: Roll number already exists")
        return False
    students.append({"name": name, "roll": roll, "class": class_name})
    print(f"Student added successfully with name is {name}")
    return True

# view student function here
def view_students(students, name, roll, class_name):
    if not students:
        print("No students found")
    else:
        for student in students:
            print(f"Name: {name}, Roll: {roll}, Class: {class_name}")

# view student function here
def delete_student(students, roll):
    for i in range(len(students)):
        if students[i]["roll"] == roll:
            removed = students.pop(i)
            print(f"Student deleted successfully with name is {removed['name']}")  # Confirmation message for deletion
            return
    print("Roll number not found")


# Main function to run the program
def main():
    students = []
    while True:
        print("\n1. Add Student")
        print("2. View List")
        print("3. Delete Student")
        print("4. Exit")
        choice = input("Choice: ")

        if choice == '1':
            name = input("Name: ")
            roll = int(input("Roll: "))
            class_name = input("Class: ")
            print("------------------------------------------------")
            add_student(students, name, roll, class_name)
            print("------------------------------------------------")
        elif choice == '2':
            print("All Students List")
            print("------------------------------------------------")
            view_students(students, name, roll, class_name)
            print("------------------------------------------------")
        elif choice == '3':
            roll = int(input("Roll number to delete: "))
            print("------------------------------------------------")
            delete_student(students, roll)
            print("------------------------------------------------")
        elif choice == '4':
            print("Program ended")
            break
        else:
            print("Invalid choice")

main()