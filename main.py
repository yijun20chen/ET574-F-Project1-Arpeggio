from data import add_grade
from tracker import view_all, view_summary

def main():
    print("Welcome to Grade Tracker! ")
    print("""
1. Add Grade 
2. View All Grades 
3. View Summary 
4. Exit 
    """)

    return int(input("Enter choice: "))

result = main()

while result != 4:
    if result == 1:
        add_grade()
        print("Option 1 chosen") # sanity check
    elif result == 2:
        view_all()
        print("Option 2 chosen")
    elif result == 3:
        view_summary()
        print("Option 3 chosen")
    else:
        print("Invalid choice. Please try again.")
    result = main()