students = []

def add_student(name,age):
    students.append({
            "name" : name,
            "age" : age
})

def show_student():
    for s in students:
      print( s) 

def average_age():
    total = 0
    for s in students:
        total += s["age"]
    return total / len(students)

add_student("anya", 18)
add_student("eed", 19)
add_student("kusu", 36)

show_student()
print("average age:" , average_age())
