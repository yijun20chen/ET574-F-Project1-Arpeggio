import data


def add_grade():
    assignment_name = input("Enter assignment name: ")
    while not assignment_name.strip():
        print("Assignment name cannot be empty.")
        assignment_name = input("Enter assignment name: ")
    data.assignment_names.append(assignment_name)

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

    data.scores.append(score)
    print("Grade Recorded!")
    return assignment_name, score

def view_all():
    if not data.assignment_names:
        print('No grades recorded.')
        return
    print('\nAll Grades:')
    for i, (name, score) in enumerate(zip(data.assignment_names, data.scores), 1):
        print(f'{i}. {name}: {score}')
def view_summary():
    """Wrapper for display_summary to allow future extension or interface consistency."""
    assignments = dict(zip(data.assignment_names, data.scores))
    return display_summary(assignments)

def display_summary(assignments):
    """Display a summary of all assignments and their scores."""
    if not assignments:
        print("No assignments recorded.")
        return
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
        print("- Average score: N/A")
        print("- Highest score: N/A")
        print("- Lowest score: N/A")