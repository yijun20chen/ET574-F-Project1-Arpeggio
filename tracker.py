def add_grade():
    assignment_name = input("Enter assignment name: ")
    while not assignment_name.strip():
        print("Assignment name cannot be empty.")
        assignment_name = input("Enter assignment name: ")

    while True:
        score_input = input("Enter assignment score: ")
        try:
            score = float(score_input)
            if score < 0:
                print("Score cannot be negative.")
                continue
            break
        except ValueError:
            print("Invalid score. Please enter a numeric value.")

    print(f"Assignment '{assignment_name}' with score {score} added.")
    return assignment_name, score

def view_all():
    pass

def view_summary():
    pass