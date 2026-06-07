# Student Class Report

def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

def get_result(percentage):
    if percentage >= 50:
        return "PASSED"
    else:
        return "FAILED"

def calculate_stats(marks):
    total = 0
    for mark in marks:
        total += mark
    percentage = round((total / 500) * 100, 2)
    average = round(total / 5, 2)
    return total, percentage, average

def get_student_data(student_number):
    print("\n--- Student", student_number, "---")
    name = input("Name: ")
    marks = []
    for i in range(1, 6):
        mark = int(input("Subject " + str(i) + ": "))
        marks.append(mark)
    total, percentage, average = calculate_stats(marks)
    grade = get_grade(percentage)
    result = get_result(percentage)
    student = {
        "name": name,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "average": average,
        "grade": grade,
        "result": result
    }
    return student

def get_all_students():
    students = []
    n = int(input("How many students? "))
    for i in range(1, n+1):
        student = get_student_data(i)
        students.append(student)
    return students

def find_topper(students):
    topper = students[0]
    for student in students:
        if student["percentage"] > topper["percentage"]:
            topper = student
    return topper

def find_weakest(students):
    weakest = students[0]
    for student in students:
        if student["percentage"] < weakest["percentage"]:
            weakest = student
    return weakest

def count_pass_fail(students):
    passed = 0
    failed = 0
    for student in students:
        if student["result"] == "PASSED":
            passed += 1
        else:
            failed += 1
    return passed, failed

def display_class_report(students):
    print("\n========= CLASS REPORT =========")
    for student in students:
        print(student["name"], "|",
              student["total"], "/500 |",
              student["percentage"], "% |",
              student["grade"], "|",
              student["result"])
    topper = find_topper(students)
    weakest = find_weakest(students)
    passed, failed = count_pass_fail(students)
    print("\nTotal Students:", len(students))
    print("Passed:", passed)
    print("Failed:", failed)
    print("Topper:", topper["name"],
          "(", topper["percentage"], "%)")
    print("Needs Improvement:", weakest["name"],
          "(", weakest["percentage"], "%)")
    print("=================================")

def main():
    students = get_all_students()      # ✅ first get students
    display_class_report(students)     # ✅ then display

main()