import csv
import random

# Makes the random numbers the same every time you run it
random.seed(42)

departments = {
    "Computer Science": "CSC",
    "Cyber Security": "CYB",
    "Information Technology": "IFT",
    "Software Engineering": "SEN",
}
levels = [100, 200, 300, 400]
entry_year = {100: 2026, 200: 2025, 300: 2024, 400: 2023}

students = []
for i in range(1, 101):  # 100 students
    dept = random.choice(list(departments))
    level = random.choice(levels)
    student_id = f"{departments[dept]}/{entry_year[level]}/{i:03d}"

    attendance = random.randint(50, 100)

    # Students who attend more tend to score higher
    score = attendance * 0.6 + random.uniform(10, 40)
    score = round(min(score, 100), 1)

    students.append([student_id, dept, level, attendance, score])

with open("student_dataset.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "Student ID",
        "Department",
        "Level",
        "Attendance Percentage",
        "Average Examination Score",
    ])
    writer.writerows(students)

print("Done! student_dataset.csv created with", len(students), "students.")
