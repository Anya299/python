students = [
    {"name": "Anya", "marks": 99},
    {"name": "kusu", "marks": 100},
    {"name": "bhoom", "marks": 99.99}
]


def average_marks(data):
    total = 0
    for s in data:
        total += s["marks"]
    return total / len(data)


def top_student(data):
    top = data[0]
    for s in data:
        if s["marks"] > top["marks"]:
            top = s
    return top


def generate_report(data):
    print("=== STUDENT REPORT ===")
    print("Average marks:", average_marks(data))
    print("Top student:", top_student(data))


generate_report(students)
