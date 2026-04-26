def write_students():
    with open("students.csv", "w") as file:
        file.write("name,marks\n")
        file.write("Anya,99\n")
        file.write("John,85\n")
        file.write("Dee,92\n")


def read_students():
    students = []

    with open("students.csv", "r") as file:
        next(file)  # skip header
        for line in file:
            name, marks = line.strip().split(",")
            students.append({
                "name": name,
                "marks": float(marks)
            })

    return students


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


# PIPELINE
write_students()
data = read_students()

print("Average:", average_marks(data))
print("Top Student:", top_student(data))
