student_records = {}

def add_student(name,age,courses):
    if name in student_records:
        print(f"Student '{name}' already exists.")
    else:
        student_records[name] = {"age": age, "grades": set(), "courses": set(courses)}
        print(f"Student '{name}' added successfully.")
    

def add_grade(name, grade):
    if name not in student_records:
        print(f"Student '{name}' not found.")
    else:
        student_records[name]["grades"].add(grade)
        print(f"Grade {grade} added for student '{name}'.")

def is_enrolled(name, course):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return False
    else:
        return True if course in student_records[name]["courses"] else False

def calculate_average_grade(name):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return None
    else:
        total = sum(student_records[name]["grades"])
        divs = len(student_records[name]["grades"])

        if divs == 0:
            return 0
        else:
            total_average = total / divs
            average_grade = float(total_average)
            return average_grade

def list_students_by_course(course):
    students_course = []
    for name in student_records:
        if course in student_records[name]["courses"]:
            students_course.append(name)
    return students_course

def filter_top_students(threshold):
    list_name = []
    for name in student_records:
        if calculate_average_grade(name) > threshold:
            list_name.append(name)
    return list_name


add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Math", "Biology"])
add_student("Diana", 23, ["Chemistry", "Physics"])
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
add_grade("Diana", 95)
print(filter_top_students(80))  # Should return ["Alice", "Diana"]
print(filter_top_students(90))  # Should return ["Diana"]
print(filter_top_students(100))  # Should return an empty list