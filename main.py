import data
from tracker import add_grade, view_all, view_summary

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
        name, score = add_grade()
        data.assignment_names.append(name)
        data.scores.append(score)
    elif result == 2:
        view_all()
    elif result == 3:
        view_summary()
    else:
        print("Invalid choice. Please try again.")
    result = main()