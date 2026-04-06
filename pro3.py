all_students = []

print("Welcome to the Student Data Organizer!")
print("---------------------------------------")

while True:
    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        # --- Student Data Collection ---
        student_id = input("Enter student ID: ")
        name = input("Name: ")
        # Type Casting: Converting string input to integer
        age = int(input("Age: ")) 
        
        grade = input("Grade: ")
        dob = input("Date of Birth (YYYY-MM-DD): ")
        subjects_input = input("Subjects (comma-separated): ")
        
        # Use a Set to ensure subjects are unique (removes duplicates)
        subjects_set = {s.strip() for s in subjects_input.split(",")}
        
        # Use a Tuple for immutable data (ID and DOB shouldn't change)
        identity_info = (student_id, dob)

        # Use a Dictionary to organize the record
        student_record = {
            "identity": identity_info,
            "name": name,
            "age": age,
            "grade": grade,
            "subjects": subjects_set
        }

        # Adding the dictionary to our main List
        all_students.append(student_record)
        print("Student added successfully!")

    elif choice == '2':
        # --- Display All (String Formatting) ---
        if not all_students:
            print("No records found.")
        else:
            print("\n--- Display All Students ---")
            for s in all_students:
                # Extracting ID from the Tuple
                current_id = s["identity"][0]
                # Formatting the Set back into a readable string
                subj_display = ", ".join(s["subjects"])
                
                # Demonstration of f-string formatting
                print(f"ID: {current_id} | Name: {s['name']} | Age: {s['age']} | Grade: {s['grade']} | Subjects: {subj_display}")

    elif choice == '3':
        # --- Update Information (Demonstrating List/Dict Mutability) ---
        search_id = input("Enter Student ID to update: ")
        found = False
        for s in all_students:
            if s["identity"][0] == search_id:
                s["age"] = int(input("Enter new age: "))
                s["grade"] = input("Enter new grade: ")
                new_subs = input("Enter new subjects (comma-separated): ")
                s["subjects"] = {sub.strip() for sub in new_subs.split(",")}
                print("Record updated successfully.")
                found = True
                break
        if not found:
            print("Student ID not found.")

    elif choice == '4':
        # --- Delete Student (Using del keyword) ---
        search_id = input("Enter Student ID to delete: ")
        found = False
        for i in range(len(all_students)):
            if all_students[i]["identity"][0] == search_id:
                del all_students[i]
                print(f"Student record {search_id} deleted.")
                found = True
                break
        if not found:
            print("Student ID not found.")

    elif choice == '5':
        # --- Unique Subjects Offered ---
        total_subjects = set()
        for s in all_students:
            total_subjects.update(s["subjects"])
        
        if total_subjects:
            print("All unique subjects offered across all students:")
            print(", ".join(total_subjects))
        else:
            print("No subjects found.")

    elif choice == '6':
        print("Thank you for using the Student Data Organizer!")
        break

    else:
        print("Invalid option. Please choose 1-6.")