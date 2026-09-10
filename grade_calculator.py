# Week 1 Mini Project
# CLI Grade Calculator


# Function to calculate grade
def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


# Function to check pass or fail
def check_result(marks):
    for mark in marks.values():
        if mark < 35:
            return "FAIL"
    return "PASS"


# Function to enter student details
def get_student_details():

    name = input("\nEnter student name: ")

    marks = {}

    subjects = ["Python", "Maths", "English", "Science", "Computer"]

    for subject in subjects:

        while True:
            try:
                mark = float(input(f"Enter marks for {subject} (0-100): "))

                if 0 <= mark <= 100:
                    marks[subject] = mark
                    break
                else:
                    print("Please enter marks between 0 and 100.")

            except ValueError:
                print("Invalid input! Please enter a number.")

    return name, marks


# Function to calculate result
def calculate_result(name, marks):

    total = sum(marks.values())

    average = total / len(marks)

    grade = calculate_grade(average)

    result = check_result(marks)

    student = {
        "Name": name,
        "Marks": marks,
        "Total": total,
        "Average": average,
        "Grade": grade,
        "Result": result
    }

    return student


# Function to display report
def display_report(student):

    print("\n==============================")
    print("       STUDENT REPORT")
    print("==============================")

    print("Name:", student["Name"])

    print("\nSubject Marks:")

    for subject, mark in student["Marks"].items():
        print(subject, ":", mark)

    print("------------------------------")

    print("Total:", student["Total"])
    print("Average:", round(student["Average"], 2))
    print("Grade:", student["Grade"])
    print("Result:", student["Result"])

    print("==============================")


# Main Program

print("================================")
print("     CLI GRADE CALCULATOR")
print("================================")

while True:

    name, marks = get_student_details()

    student = calculate_result(name, marks)

    display_report(student)

    choice = input("\nDo you want to calculate another student? (yes/no): ")

    if choice.lower() != "yes":
        print("\nThank you for using Grade Calculator!")
        break