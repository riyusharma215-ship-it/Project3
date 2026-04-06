# Project3

Gemini said
Student Data Organizer
A robust Python-based Command-Line Interface (CLI) application designed to manage student records efficiently. This project serves as a practical demonstration of Python's core data structures—Lists, Dictionaries, Tuples, and Sets—to perform comprehensive CRUD (Create, Read, Update, Delete) operations.

## Key Features
Comprehensive Record Creation: Collects and organizes student ID, name, age, grade, date of birth, and subjects.

Data Integrity via Types:

Tuples: Used for immutable "identity" data (Student ID and Date of Birth) to ensure core identifiers remain unchanged.

Sets: Utilized for subjects to automatically handle comma-separated input and eliminate duplicate entries.

Dynamic Record Management:

Update: Modify a student's age, grade, or subject list by searching for their unique ID.

Delete: Permanently remove a specific student record from the database using the del keyword.

Global Data Insights: A specialized feature to aggregate and display all unique subjects offered across the entire student body.

User-Friendly Interface: Employs a persistent while loop menu with clear prompts and f-string formatted output for readability.

## Technical Implementation
The script pro3.py utilizes the following Python fundamentals:

Component	Purpose
Lists	all_students stores the collection of all student record dictionaries.
Dictionaries	Each student's data is mapped to descriptive keys (e.g., "name", "age").
Type Casting	Converts string input() into int for numerical values like age.
String Methods	Uses .strip() and .split(",") to clean and parse user input.
Join Method	Converts internal Sets and Lists back into readable, comma-separated strings for display.
## Usage Guide
Add Student (Option 1): Enter the requested details. Multiple subjects can be entered separated by commas (e.g., "Math, Science").

Display All (Option 2): Lists every student currently in the system with their formatted details.

Update (Option 3): Search for a student by ID to change their age, grade, or subjects.

Delete (Option 4): Provide a Student ID to remove their record from the list.

Unique Subjects (Option 5): Displays a consolidated list of every unique subject being studied by all registered students.

Exit (Option 6): Safely closes the application.

https://drive.google.com/file/d/1zUY07XVuIwyKFnSCi_Q4QQORHf2Y7VEf/view?usp=drive_link
