# Student information using Dictionary, Tuple, and List

# Tuple: attributes of a student
student1 = (101, "Aditya", "CSE", 85)
student2 = (102, "Rahul", "ECE", 78)
student3 = (103, "Priya", "IT", 92)

# List: store multiple student tuples
students_list = [student1, student2, student3]

# Dictionary: store student records using Roll Number as the key
students = {
    student[0]: student for student in students_list
}

# 1. Add a new student record
students[104] = (104, "Sneha", "ME", 88)

# 2. Delete an existing student record
del students[102]

# 3. Update the details of a student
students[103] = (103, "Priya", "IT", 95)

# 4. Display the final student records
print("Final Student Records:")
print("-" * 50)

for roll_no, details in students.items():
    print("Roll Number:", details[0])
    print("Name:", details[1])
    print("Branch:", details[2])
    print("Marks:", details[3])
    print("-" * 50)
