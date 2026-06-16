# Smart Exam Seating Arrangement System with Hall Allocation

import random

# Student Data
students = [
    ["101", "Ravi", "CSE"],
    ["102", "Priya", "ECE"],
    ["103", "Arjun", "MECH"],
    ["104", "Sneha", "CSE"],
    ["105", "Kiran", "ECE"],
    ["106", "Divya", "MECH"],
    ["107", "Rahul", "CSE"],
    ["108", "Anjali", "ECE"],
    ["109", "Vikas", "MECH"],
    ["110", "Pooja", "CSE"],
    ["111", "Manoj", "ECE"],
    ["112", "Keerthi", "MECH"]
]

# Shuffle Students
random.shuffle(students)

# Hall Information
halls = {
    "Hall-A": 6,
    "Hall-B": 6
}

# Hall Allocation
hall_allocation = {}
student_index = 0

for hall, capacity in halls.items():
    hall_allocation[hall] = []

    for i in range(capacity):
        if student_index < len(students):
            hall_allocation[hall].append(students[student_index])
            student_index += 1

# Display Hall Allocation
print("\n===== HALL ALLOCATION =====\n")

for hall in hall_allocation:
    print(f"\n{hall}")
    print("-" * 30)

    for student in hall_allocation[hall]:
        print(
            f"Roll No: {student[0]} | "
            f"Name: {student[1]} | "
            f"Branch: {student[2]}"
        )

# Seating Arrangement for Each Hall
rows = 2
cols = 3

print("\n\n===== SEATING ARRANGEMENT =====\n")

for hall in hall_allocation:

    print(f"\n{hall}")
    print("=" * 30)

    seating = [[None for j in range(cols)] for i in range(rows)]

    index = 0
    students_in_hall = hall_allocation[hall]

    for i in range(rows):
        for j in range(cols):
            if index < len(students_in_hall):
                seating[i][j] = students_in_hall[index]
                index += 1

    for i in range(rows):
        for j in range(cols):
            if seating[i][j]:
                print(
                    f"{seating[i][j][0]}-{seating[i][j][2]}",
                    end="\t"
                )
        print()

# Detailed Seat Allocation
print("\n\n===== DETAILED SEAT ALLOCATION =====\n")

for hall in hall_allocation:

    print(f"\n{hall}")
    print("-" * 40)

    seat_no = 1

    for student in hall_allocation[hall]:
        print(
            f"Seat {seat_no}: "
            f"Roll No = {student[0]}, "
            f"Name = {student[1]}, "
            f"Branch = {student[2]}"
        )
        seat_no += 1