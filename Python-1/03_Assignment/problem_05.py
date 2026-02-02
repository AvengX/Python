students = {}

while True:
    print("\nMenu:")
    print("A - Add a student")
    print("B - Update marks")
    print("C - Search for a student")
    print("D - Display all students and marks")
    print("Q - Quit")
    
    choice = input("Enter your choice: ").upper()
    
    if choice == 'A':
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks
    elif choice == 'B':
        name = input("Enter student name to update: ")
        if name in students:
            marks = int(input("Enter new marks: "))
            students[name] = marks
        else:
            print("Student not found.")
    elif choice == 'C':
        name = input("Enter student name to search: ")
        if name in students:
            print(f"{name} has {students[name]} marks.")
        else:
            print("Student not found.")
    elif choice == 'D':
        for name, marks in students.items():
            print(f"Name: {name}, Marks: {marks}")
    elif choice == 'Q':
        break
    else:
        print("Invalid choice.")