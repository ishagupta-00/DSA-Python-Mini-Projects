# -------------------- STUDENT MARKS ANALYZER --------------------

def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


def main():

    students = []

    print("========== STUDENT MARKS ANALYZER ==========")

    try:
        total_students = int(input("Enter number of students: "))

        if total_students <= 0:
            print("Number of students must be greater than 0.")
            return

        for i in range(total_students):

            print("\nStudent", i + 1)

            name = input("Enter student name: ").strip()

            while name == "":
                print("Name cannot be empty.")
                name = input("Enter student name: ").strip()

            marks = float(input("Enter marks (0-100): "))

            while marks < 0 or marks > 100:
                print("Marks must be between 0 and 100.")
                marks = float(input("Enter marks (0-100): "))

            grade = calculate_grade(marks)

            student = {
                "name": name,
                "marks": marks,
                "grade": grade
            }

            students.append(student)

        # Calculate average
        total_marks = 0

        for student in students:
            total_marks += student["marks"]

        average = total_marks / len(students)

        # Find highest scorer
        highest = students[0]

        for student in students:
            if student["marks"] > highest["marks"]:
                highest = student

        # Display results
        print("\n========== RESULT ==========")

        for student in students:
            print("\nName:", student["name"])
            print("Marks:", student["marks"])
            print("Grade:", student["grade"])

            if student["marks"] >= 50:
                print("Status: Pass")

                if student["marks"] >= 80:
                    print("Keep it up! Great performance.")
            else:
                print("Status: Fail")

        print("\n========== CLASS SUMMARY ==========")
        print("Average Marks:", round(average, 2))
        print("Highest Scorer:", highest["name"])
        print("Highest Marks:", highest["marks"])


    except ValueError:
        print("Please enter valid numbers.")


main()