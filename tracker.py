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

def view_all(assignments):
    if not assignments:
        print("No assignments recorded.")
        return
def view_summary(assignments):
    """Display a summary of all assignments and their scores."""
    if not assignments:
        print("No assignments recorded.")
        return
    print("Assignments and scores:")
    for name, score in assignments.items():
        print(f"- {name}: {score}")
    scores = list(assignments.values())
    print("Summary:")
    print(f"- Total assignments: {len(assignments)}")
    print(f"- Average score: {sum(scores) / len(scores):.2f}")
    print(f"- Highest score: {max(scores)}")
    print(f"- Lowest score: {min(scores)}")
    print("Assignments and scores:")
    for name, score in assignments.items():
        print(f"- {name}: {score}")